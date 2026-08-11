---
id: linux-man-pages-options-top-https-man7-org-linux-man-pages-man1-ac-1-html-to-16c19016
type: concept
title: OPTIONS         [top](https://man7.org/linux/man-pages/man1/ac.1.html#top_of_page)
description: '```'
category: linux-man-pages
tags: []
source:
  name: linux-man-pages
  url: https://man7.org/linux/man-pages/man1/ac.1.html
updated_at: '2026-08-11'
created_at: '2026-08-11'
---

## OPTIONS         [top](https://man7.org/linux/man-pages/man1/ac.1.html#top_of_page)

```
       -d, --daily-totals
              Print totals for each day rather than just one big total at
              the end.  The output looks like this:
                      Jul  3  total     1.17
                      Jul  4  total     2.10
                      Jul  5  total     8.23
                      Jul  6  total     2.10
                      Jul  7  total     0.30
       -p, --individual-totals
              Print time totals for each user in addition to the usual
              everything-lumped-into-one value.  It looks like:
                      bob       8.06
                      goff      0.60
                      maley     7.37
                      root      0.12
                      total    16.15
       people Print out the sum total of the connect time used by all of
              the users included in people.  Note that people is a space
              separated list of valid user names; wildcards are not al‐
              lowed.
       -f, --file filename
              Read from the file filename instead of the system's wtmp
              file.
       --complain
              When the wtmp file has a problem (a time-warp, missing
              record, or whatever), print out an appropriate error.
       --reboots
              Reboot records are NOT written at the time of a reboot, but
              when the system restarts; therefore, it is impossible to
              know exactly when the reboot occurred.  Users may have been
              logged into the system at the time of the reboot, and many
              ac's automatically count the time between the login and the
              reboot record against the user (even though all of that
              time shouldn't be, perhaps, if the system is down for a
              long time, for instance).  If you want to count this time,
              include the flag.  *For vanilla ac compatibility, include
              this flag.*
       --supplants
              Sometimes, a logout record is not written for a specific
              terminal, so the time that the last user accrued cannot be
              calculated.  If you want to include the time from the
              user's login to the next login on the terminal (though
              probably incorrect), include this you want to include the
              time from the user's login to the next login on the termi‐
              nal (though probably incorrect), include this flag.  *For
              vanilla ac compatibility, include this flag.*
       --timewarps
              Sometimes, entries in a wtmp file will suddenly jump back
              into the past without a clock change record occurring.  It
              is impossible to know how long a user was logged in when
              this occurs.  If you want to count the time between the lo‐
              gin and the time warp against the user, include this flag.
              *For vanilla ac compatibility, include this flag.*
       --compatibility
              This is shorthand for typing out the three above options.
       -a, --all-days
              If we're printing daily totals, print a record for every
              day instead of skipping intervening days where there is no
              login activity.  Without this flag, time accrued during
              those intervening days gets listed under the next day where
              there is login activity.
       --tw-leniency num
              Set the time warp leniency to num seconds.  Records in wtmp
              files might be slightly out of order (most notably when two
              logins occur within a one-second period - the second one
              gets written first).  By default, this value is set to 60.
              If the program notices this problem, time is not assigned
              to users unless the --timewarps flag is used.
       --tw-suspicious num
              Set the time warp