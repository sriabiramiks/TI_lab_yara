rule hidden_bee : bee
{
    meta:
        description = "This rule is written for 2018-08-Hidden-Bee-Elements."
        threat_level = 1
        in_the_wild = true

    strings:
        $a = "wireshark.exe"
        $b = "EHSniffer.exe"
        $c = "dllhost.exe"
        $d = "kernel32.dll"
        $e = "ntdll.dll"

    condition:
        $a or $b or $c or $d or $e
}