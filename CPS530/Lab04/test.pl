#!/usr/bin/perl
    use strict;
    use warnings;
    use CGI;
    my $q = new CGI;
    print $q->header,
          $q->start_html('Your page title'),
          'Some plain text',
          $q->b('Some bold text'),
          $q->end_html;