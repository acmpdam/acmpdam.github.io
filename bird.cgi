#!/usr/bin/env perl
use strict;
use CGI;
my $page = CGI -> new();
print $page->header();
print <<ENDHTML;
<head>
</head>
<body>
<h1> SNAKE </h1>
</body>
ENDHTML




