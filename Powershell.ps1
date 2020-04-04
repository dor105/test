Function Get-ComputerInformation
{
    ## Computer Sys
    Get-WmiObject -Class Win32_ComputerSystem
    ## Operating Sys
    Get-WmiObject -class win32_OperatingSystem
    ## Bios
    Get-WmiObject -class win32_BIOS
}