#!/usr/bin/env perl
open(BIB, 'publications.bib');
while ($line = <BIB>) {
    if ($line =~ /^\@article/) {
	#print $line;
	$line =~ s/\@article\{//;
	$line =~ s/,\n//;
	print "cite\{", $line, "\}\n";
    }
}
exit;
