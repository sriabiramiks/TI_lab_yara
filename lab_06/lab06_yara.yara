rule Melissa_Virus
{
    meta:
        description = "Melissa virus"
        file_type = "VBA"
        malware_type = "Virus"

    strings:
        $a = "WORD/Melissa written by Kwyjibo"
        $b = "Works in both Word 2000 and Word 97"
		$c = "Worm? Macro Virus? Word 97 Virus? Word 2000 Virus? You Decide!"
        $d = "Word -> Email | Word 97 <--> Word 2000 ... it's a new age!"
    
    condition:
        all of ($*)
}