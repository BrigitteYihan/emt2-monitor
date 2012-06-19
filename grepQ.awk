BEGIN { }
{
    if ($1 == run) {
	print $3
    }
}
END {}

