provider "virtualbox" {
  version = "1.0.0"
}

resource "virtualbox_instance" "example" {
  name = "oracle-linux-vm"
  vram = "32"
  memory = "4096"
  cpus = "1"
  iso_path = "/Users/antoniosergiofigueiredo/Downloads/OracleLinux-R8-U6-x86_64-dvd.iso"
  boot_command = [
    "install",
    "text",
    "console=tty0",
    "console=ttyS0,115200n8",
    "root=live:CDLABEL=OracleLinux-R8-U6-x86_64-dvd",
    "rootfstype=auto",
    "ro",
    "rhgb",
    "quiet",
    "LANG=en_US.UTF-8",
    "inst.text",
    "inst.stage2=hd:LABEL=OracleLinux-R8-U6-x86_64-dvd"
  ]
}
