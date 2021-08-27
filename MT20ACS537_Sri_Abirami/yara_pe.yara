rule hidden_bee
{
    meta:
        author = "Sri Abirami K S"
	    creationdate = "Aug 21, 2021"
        description = "This rule is written for 2018-08-Hidden-Bee-Elements."

    strings:
        $a = "QQV"
        $b = "KERNEL32.dll"
        $c = "ntdll.dll"
        $d = "MSVCRT.dll"
        $e = "WSP"
        $f = "SVW"
        $g = "SSS"
        $h = "RtlGetNtVersionNumbers"

    condition:
        all of ($*)
}