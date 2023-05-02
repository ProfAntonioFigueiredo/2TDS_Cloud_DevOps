WITH first_loan_date as (
    SELECT
        TELCO_ID,
        UUID,
        CAST(ISSUED_DATE AS DATE) AS date
    FROM "SOURCE_DATA"."TIMBRAZIL"."LEND_LOANS"
    WHERE lender = 'Juvo'
    QUALIFY ROW_NUMBER() OVER(PARTITION BY UUID ORDER BY ISSUED_DATE) = 1
),

borrowers as (
    SELECT
        a.TELCO_ID,
        b.date,
        COUNT(DISTINCT a.UUID) AS borrowers,
        COUNT(DISTINCT CASE WHEN c.STATUS IN ('active', 'inactive') THEN c.UUID END) AS active_borrowers    
    FROM "SOURCE_DATA"."TIMBRAZIL"."LEND_LOANS" a
    INNER JOIN first_loan_date b ON a.TELCO_ID=b.TELCO_ID AND a.UUID=b.UUID
    LEFT JOIN common_dim_subscribers c ON a.TELCO_ID=c.TELCO_ID AND a.UUID=c.UUID
    WHERE a.lender = 'Juvo'
    GROUP BY 1, 2  
),

not_ussd_wapp AS (
    SELECT
        a.uuid,
        b.active,
        MIN(a.JUVO_REGISTRATION_DATE) as created_at
    FROM common_dim_subscribers a
    JOIN common_cbr_registrations_users b ON a.uuid=b.uuid
    WHERE   a.telco_id = 'TIMBRAZIL'
        AND a.uuid IS NOT NULL
        AND a.JUVO_REGISTRATION_DATE IS NOT NULL
        AND b.main_channel NOT IN ('ussd', 'wapp')
    GROUP BY 1, 2
),

ussd_wapp AS (
    SELECT
        a.uuid,
        b.active,
        MIN(a.issued_date) as created_at
    FROM "SOURCE_DATA"."TIMBRAZIL"."LEND_LOANS" a
    JOIN common_cbr_registrations_users b ON a.uuid=b.uuid AND a.channel=b.main_channel
    WHERE   a.telco_id = 'TIMBRAZIL'
        AND a.lender = 'Juvo'
        AND b.main_channel IN ('ussd', 'wapp')
    GROUP BY 1, 2
),

post_launch_users AS (
    SELECT
        uuid,
        active,
        created_at AS registr_date
    FROM (
            SELECT * FROM not_ussd_wapp
            UNION ALL
            SELECT * FROM ussd_wapp
         )
),

registrations AS (
    SELECT
        'TIMBRAZIL' AS TELCO_ID,
        CAST(registr_date AS DATE) AS date,
        COUNT(DISTINCT uuid) AS users,
        COUNT(DISTINCT CASE WHEN active THEN uuid END) AS active_users
    FROM post_launch_users
    GROUP BY 1, 2    
    
    UNION ALL
    
    SELECT
        TELCO_ID,
        CAST(juvo_registration_date AS DATE) AS date,
        COUNT(DISTINCT uuid) AS users,
        COUNT(DISTINCT CASE WHEN STATUS IN ('active', 'inactive') THEN uuid END) AS active_users
    FROM common_dim_subscribers
    WHERE telco_id = 'TIMBRAZIL' AND juvo_registration_date IS NOT NULL
    GROUP BY 1, 2
)

select
	b.telco_id,
    b.date,
    b.borrowers,
    b.active_borrowers,
    r.users,
    r.active_users,
    sum(borrowers) over (partition by b.telco_id order by b.date asc rows unbounded preceding) as cumulative_borrowers,
    sum(active_borrowers) over (partition by b.telco_id order by b.date asc rows unbounded preceding) as cumulative_active_borrowers,
    sum(users) over (partition by b.telco_id order by b.date asc rows unbounded preceding) as cumulative_users,
    sum(active_users) over (partition by b.telco_id order by b.date asc rows unbounded preceding) as cumulative_active_users
from borrowers b
left join registrations r on b.telco_id = r.telco_id and b.date = r.date