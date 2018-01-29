#!/bin/bash

set -e
set -x

if [ -z "$CC" ]; then
    CC="/usr/bin/gcc"
fi

# eid=10
export MAKEFLAGS=w
export MAKELEVEL=3
export MFLAGS=-w
export PWD=/home/kupsch/build/pkg1/lighttpd-1.4.45/src
export SHLVL=4
export _=/usr/bin/gcc

cd /home/kupsch/build/pkg1/lighttpd-1.4.45/src

$CC -g -O2 -o lemon ./lemon.c

# eid=65
export DUALCASE=1
export MAKELEVEL=4
export SHLVL=6

$CC -DHAVE_CONFIG_H -DHAVE_VERSION_H '-DLIBRARY_DIR="/usr/local/lib"' '-DSBIN_DIR="/usr/local/sbin"' -I. -I.. -D_REENTRANT -D__EXTENSIONS__ -D_FILE_OFFSET_BITS=64 -D_LARGEFILE_SOURCE -D_LARGE_FILES -g -O2 -Wall -W -Wshadow -pedantic -std=gnu99 -MT mod_flv_streaming.lo -MD -MP -MF .deps/mod_flv_streaming.Tpo -c mod_flv_streaming.c -fPIC -DPIC -o .libs/mod_flv_streaming.o

# eid=82
export LANG=C

$CC -shared -fPIC -DPIC .libs/mod_flv_streaming.o -g -O2 -Wl,-soname -Wl,mod_flv_streaming.so -o .libs/mod_flv_streaming.so

# eid=124
export LANG=en_US.UTF-8

$CC -DHAVE_CONFIG_H -DHAVE_VERSION_H '-DLIBRARY_DIR="/usr/local/lib"' '-DSBIN_DIR="/usr/local/sbin"' -I. -I.. -D_REENTRANT -D__EXTENSIONS__ -D_FILE_OFFSET_BITS=64 -D_LARGEFILE_SOURCE -D_LARGE_FILES -g -O2 -Wall -W -Wshadow -pedantic -std=gnu99 -MT mod_evasive.lo -MD -MP -MF .deps/mod_evasive.Tpo -c mod_evasive.c -fPIC -DPIC -o .libs/mod_evasive.o

# eid=141
export LANG=C

$CC -shared -fPIC -DPIC .libs/mod_evasive.o -g -O2 -Wl,-soname -Wl,mod_evasive.so -o .libs/mod_evasive.so

# eid=183
export LANG=en_US.UTF-8

$CC -DHAVE_CONFIG_H -DHAVE_VERSION_H '-DLIBRARY_DIR="/usr/local/lib"' '-DSBIN_DIR="/usr/local/sbin"' -I. -I.. -D_REENTRANT -D__EXTENSIONS__ -D_FILE_OFFSET_BITS=64 -D_LARGEFILE_SOURCE -D_LARGE_FILES -g -O2 -Wall -W -Wshadow -pedantic -std=gnu99 -MT mod_webdav_la-mod_webdav.lo -MD -MP -MF .deps/mod_webdav_la-mod_webdav.Tpo -c mod_webdav.c -fPIC -DPIC -o .libs/mod_webdav_la-mod_webdav.o

# eid=200
export LANG=C

$CC -shared -fPIC -DPIC .libs/mod_webdav_la-mod_webdav.o -g -O2 -Wl,-soname -Wl,mod_webdav.so -o .libs/mod_webdav.so

# eid=242
export LANG=en_US.UTF-8

$CC -DHAVE_CONFIG_H -DHAVE_VERSION_H '-DLIBRARY_DIR="/usr/local/lib"' '-DSBIN_DIR="/usr/local/sbin"' -I. -I.. -D_REENTRANT -D__EXTENSIONS__ -D_FILE_OFFSET_BITS=64 -D_LARGEFILE_SOURCE -D_LARGE_FILES -g -O2 -Wall -W -Wshadow -pedantic -std=gnu99 -MT mod_cgi.lo -MD -MP -MF .deps/mod_cgi.Tpo -c mod_cgi.c -fPIC -DPIC -o .libs/mod_cgi.o

# eid=259
export LANG=C

$CC -shared -fPIC -DPIC .libs/mod_cgi.o -g -O2 -Wl,-soname -Wl,mod_cgi.so -o .libs/mod_cgi.so

# eid=301
export LANG=en_US.UTF-8

$CC -DHAVE_CONFIG_H -DHAVE_VERSION_H '-DLIBRARY_DIR="/usr/local/lib"' '-DSBIN_DIR="/usr/local/sbin"' -I. -I.. -D_REENTRANT -D__EXTENSIONS__ -D_FILE_OFFSET_BITS=64 -D_LARGEFILE_SOURCE -D_LARGE_FILES -g -O2 -Wall -W -Wshadow -pedantic -std=gnu99 -MT mod_scgi.lo -MD -MP -MF .deps/mod_scgi.Tpo -c mod_scgi.c -fPIC -DPIC -o .libs/mod_scgi.o

# eid=318
export LANG=C

$CC -shared -fPIC -DPIC .libs/mod_scgi.o -g -O2 -Wl,-soname -Wl,mod_scgi.so -o .libs/mod_scgi.so

# eid=360
export LANG=en_US.UTF-8

$CC -DHAVE_CONFIG_H -DHAVE_VERSION_H '-DLIBRARY_DIR="/usr/local/lib"' '-DSBIN_DIR="/usr/local/sbin"' -I. -I.. -D_REENTRANT -D__EXTENSIONS__ -D_FILE_OFFSET_BITS=64 -D_LARGEFILE_SOURCE -D_LARGE_FILES -g -O2 -Wall -W -Wshadow -pedantic -std=gnu99 -MT mod_staticfile.lo -MD -MP -MF .deps/mod_staticfile.Tpo -c mod_staticfile.c -fPIC -DPIC -o .libs/mod_staticfile.o

# eid=377
export LANG=C

$CC -shared -fPIC -DPIC .libs/mod_staticfile.o -g -O2 -Wl,-soname -Wl,mod_staticfile.so -o .libs/mod_staticfile.so

# eid=419
export LANG=en_US.UTF-8

$CC -DHAVE_CONFIG_H -DHAVE_VERSION_H '-DLIBRARY_DIR="/usr/local/lib"' '-DSBIN_DIR="/usr/local/sbin"' -I. -I.. -D_REENTRANT -D__EXTENSIONS__ -D_FILE_OFFSET_BITS=64 -D_LARGEFILE_SOURCE -D_LARGE_FILES -g -O2 -Wall -W -Wshadow -pedantic -std=gnu99 -MT mod_dirlisting.lo -MD -MP -MF .deps/mod_dirlisting.Tpo -c mod_dirlisting.c -fPIC -DPIC -o .libs/mod_dirlisting.o

# eid=436
export LANG=C

$CC -shared -fPIC -DPIC .libs/mod_dirlisting.o -lpcre -g -O2 -Wl,-soname -Wl,mod_dirlisting.so -o .libs/mod_dirlisting.so

# eid=478
export LANG=en_US.UTF-8

$CC -DHAVE_CONFIG_H -DHAVE_VERSION_H '-DLIBRARY_DIR="/usr/local/lib"' '-DSBIN_DIR="/usr/local/sbin"' -I. -I.. -D_REENTRANT -D__EXTENSIONS__ -D_FILE_OFFSET_BITS=64 -D_LARGEFILE_SOURCE -D_LARGE_FILES -g -O2 -Wall -W -Wshadow -pedantic -std=gnu99 -MT mod_indexfile.lo -MD -MP -MF .deps/mod_indexfile.Tpo -c mod_indexfile.c -fPIC -DPIC -o .libs/mod_indexfile.o

# eid=495
export LANG=C

$CC -shared -fPIC -DPIC .libs/mod_indexfile.o -g -O2 -Wl,-soname -Wl,mod_indexfile.so -o .libs/mod_indexfile.so

# eid=537
export LANG=en_US.UTF-8

$CC -DHAVE_CONFIG_H -DHAVE_VERSION_H '-DLIBRARY_DIR="/usr/local/lib"' '-DSBIN_DIR="/usr/local/sbin"' -I. -I.. -D_REENTRANT -D__EXTENSIONS__ -D_FILE_OFFSET_BITS=64 -D_LARGEFILE_SOURCE -D_LARGE_FILES -g -O2 -Wall -W -Wshadow -pedantic -std=gnu99 -MT mod_setenv.lo -MD -MP -MF .deps/mod_setenv.Tpo -c mod_setenv.c -fPIC -DPIC -o .libs/mod_setenv.o

# eid=554
export LANG=C

$CC -shared -fPIC -DPIC .libs/mod_setenv.o -g -O2 -Wl,-soname -Wl,mod_setenv.so -o .libs/mod_setenv.so

# eid=596
export LANG=en_US.UTF-8

$CC -DHAVE_CONFIG_H -DHAVE_VERSION_H '-DLIBRARY_DIR="/usr/local/lib"' '-DSBIN_DIR="/usr/local/sbin"' -I. -I.. -D_REENTRANT -D__EXTENSIONS__ -D_FILE_OFFSET_BITS=64 -D_LARGEFILE_SOURCE -D_LARGE_FILES -g -O2 -Wall -W -Wshadow -pedantic -std=gnu99 -MT mod_alias.lo -MD -MP -MF .deps/mod_alias.Tpo -c mod_alias.c -fPIC -DPIC -o .libs/mod_alias.o

# eid=613
export LANG=C

$CC -shared -fPIC -DPIC .libs/mod_alias.o -g -O2 -Wl,-soname -Wl,mod_alias.so -o .libs/mod_alias.so

# eid=655
export LANG=en_US.UTF-8

$CC -DHAVE_CONFIG_H -DHAVE_VERSION_H '-DLIBRARY_DIR="/usr/local/lib"' '-DSBIN_DIR="/usr/local/sbin"' -I. -I.. -D_REENTRANT -D__EXTENSIONS__ -D_FILE_OFFSET_BITS=64 -D_LARGEFILE_SOURCE -D_LARGE_FILES -g -O2 -Wall -W -Wshadow -pedantic -std=gnu99 -MT mod_userdir.lo -MD -MP -MF .deps/mod_userdir.Tpo -c mod_userdir.c -fPIC -DPIC -o .libs/mod_userdir.o

# eid=672
export LANG=C

$CC -shared -fPIC -DPIC .libs/mod_userdir.o -g -O2 -Wl,-soname -Wl,mod_userdir.so -o .libs/mod_userdir.so

# eid=714
export LANG=en_US.UTF-8

$CC -DHAVE_CONFIG_H -DHAVE_VERSION_H '-DLIBRARY_DIR="/usr/local/lib"' '-DSBIN_DIR="/usr/local/sbin"' -I. -I.. -D_REENTRANT -D__EXTENSIONS__ -D_FILE_OFFSET_BITS=64 -D_LARGEFILE_SOURCE -D_LARGE_FILES -g -O2 -Wall -W -Wshadow -pedantic -std=gnu99 -MT mod_rrdtool.lo -MD -MP -MF .deps/mod_rrdtool.Tpo -c mod_rrdtool.c -fPIC -DPIC -o .libs/mod_rrdtool.o

# eid=731
export LANG=C

$CC -shared -fPIC -DPIC .libs/mod_rrdtool.o -g -O2 -Wl,-soname -Wl,mod_rrdtool.so -o .libs/mod_rrdtool.so

# eid=773
export LANG=en_US.UTF-8

$CC -DHAVE_CONFIG_H -DHAVE_VERSION_H '-DLIBRARY_DIR="/usr/local/lib"' '-DSBIN_DIR="/usr/local/sbin"' -I. -I.. -D_REENTRANT -D__EXTENSIONS__ -D_FILE_OFFSET_BITS=64 -D_LARGEFILE_SOURCE -D_LARGE_FILES -g -O2 -Wall -W -Wshadow -pedantic -std=gnu99 -MT mod_usertrack.lo -MD -MP -MF .deps/mod_usertrack.Tpo -c mod_usertrack.c -fPIC -DPIC -o .libs/mod_usertrack.o

# eid=790
export LANG=C

$CC -shared -fPIC -DPIC .libs/mod_usertrack.o -g -O2 -Wl,-soname -Wl,mod_usertrack.so -o .libs/mod_usertrack.so

# eid=832
export LANG=en_US.UTF-8

$CC -DHAVE_CONFIG_H -DHAVE_VERSION_H '-DLIBRARY_DIR="/usr/local/lib"' '-DSBIN_DIR="/usr/local/sbin"' -I. -I.. -D_REENTRANT -D__EXTENSIONS__ -D_FILE_OFFSET_BITS=64 -D_LARGEFILE_SOURCE -D_LARGE_FILES -g -O2 -Wall -W -Wshadow -pedantic -std=gnu99 -MT mod_proxy.lo -MD -MP -MF .deps/mod_proxy.Tpo -c mod_proxy.c -fPIC -DPIC -o .libs/mod_proxy.o

# eid=849
export LANG=C

$CC -shared -fPIC -DPIC .libs/mod_proxy.o -g -O2 -Wl,-soname -Wl,mod_proxy.so -o .libs/mod_proxy.so

# eid=891
export LANG=en_US.UTF-8

$CC -DHAVE_CONFIG_H -DHAVE_VERSION_H '-DLIBRARY_DIR="/usr/local/lib"' '-DSBIN_DIR="/usr/local/sbin"' -I. -I.. -D_REENTRANT -D__EXTENSIONS__ -D_FILE_OFFSET_BITS=64 -D_LARGEFILE_SOURCE -D_LARGE_FILES -g -O2 -Wall -W -Wshadow -pedantic -std=gnu99 -MT mod_ssi_exprparser.lo -MD -MP -MF .deps/mod_ssi_exprparser.Tpo -c mod_ssi_exprparser.c -fPIC -DPIC -o .libs/mod_ssi_exprparser.o

# eid=931
$CC -DHAVE_CONFIG_H -DHAVE_VERSION_H '-DLIBRARY_DIR="/usr/local/lib"' '-DSBIN_DIR="/usr/local/sbin"' -I. -I.. -D_REENTRANT -D__EXTENSIONS__ -D_FILE_OFFSET_BITS=64 -D_LARGEFILE_SOURCE -D_LARGE_FILES -g -O2 -Wall -W -Wshadow -pedantic -std=gnu99 -MT mod_ssi_expr.lo -MD -MP -MF .deps/mod_ssi_expr.Tpo -c mod_ssi_expr.c -fPIC -DPIC -o .libs/mod_ssi_expr.o

# eid=971
$CC -DHAVE_CONFIG_H -DHAVE_VERSION_H '-DLIBRARY_DIR="/usr/local/lib"' '-DSBIN_DIR="/usr/local/sbin"' -I. -I.. -D_REENTRANT -D__EXTENSIONS__ -D_FILE_OFFSET_BITS=64 -D_LARGEFILE_SOURCE -D_LARGE_FILES -g -O2 -Wall -W -Wshadow -pedantic -std=gnu99 -MT mod_ssi.lo -MD -MP -MF .deps/mod_ssi.Tpo -c mod_ssi.c -fPIC -DPIC -o .libs/mod_ssi.o

# eid=988
export LANG=C

$CC -shared -fPIC -DPIC .libs/mod_ssi_exprparser.o .libs/mod_ssi_expr.o .libs/mod_ssi.o -g -O2 -Wl,-soname -Wl,mod_ssi.so -o .libs/mod_ssi.so

# eid=1030
export LANG=en_US.UTF-8

$CC -DHAVE_CONFIG_H -DHAVE_VERSION_H '-DLIBRARY_DIR="/usr/local/lib"' '-DSBIN_DIR="/usr/local/sbin"' -I. -I.. -D_REENTRANT -D__EXTENSIONS__ -D_FILE_OFFSET_BITS=64 -D_LARGEFILE_SOURCE -D_LARGE_FILES -g -O2 -Wall -W -Wshadow -pedantic -std=gnu99 -MT mod_secdownload.lo -MD -MP -MF .deps/mod_secdownload.Tpo -c mod_secdownload.c -fPIC -DPIC -o .libs/mod_secdownload.o

# eid=1047
export LANG=C

$CC -shared -fPIC -DPIC .libs/mod_secdownload.o -g -O2 -Wl,-soname -Wl,mod_secdownload.so -o .libs/mod_secdownload.so

# eid=1089
export LANG=en_US.UTF-8

$CC -DHAVE_CONFIG_H -DHAVE_VERSION_H '-DLIBRARY_DIR="/usr/local/lib"' '-DSBIN_DIR="/usr/local/sbin"' -I. -I.. -D_REENTRANT -D__EXTENSIONS__ -D_FILE_OFFSET_BITS=64 -D_LARGEFILE_SOURCE -D_LARGE_FILES -g -O2 -Wall -W -Wshadow -pedantic -std=gnu99 -MT mod_expire.lo -MD -MP -MF .deps/mod_expire.Tpo -c mod_expire.c -fPIC -DPIC -o .libs/mod_expire.o

# eid=1106
export LANG=C

$CC -shared -fPIC -DPIC .libs/mod_expire.o -g -O2 -Wl,-soname -Wl,mod_expire.so -o .libs/mod_expire.so

# eid=1148
export LANG=en_US.UTF-8

$CC -DHAVE_CONFIG_H -DHAVE_VERSION_H '-DLIBRARY_DIR="/usr/local/lib"' '-DSBIN_DIR="/usr/local/sbin"' -I. -I.. -D_REENTRANT -D__EXTENSIONS__ -D_FILE_OFFSET_BITS=64 -D_LARGEFILE_SOURCE -D_LARGE_FILES -g -O2 -Wall -W -Wshadow -pedantic -std=gnu99 -MT mod_evhost.lo -MD -MP -MF .deps/mod_evhost.Tpo -c mod_evhost.c -fPIC -DPIC -o .libs/mod_evhost.o

# eid=1165
export LANG=C

$CC -shared -fPIC -DPIC .libs/mod_evhost.o -g -O2 -Wl,-soname -Wl,mod_evhost.so -o .libs/mod_evhost.so

# eid=1207
export LANG=en_US.UTF-8

$CC -DHAVE_CONFIG_H -DHAVE_VERSION_H '-DLIBRARY_DIR="/usr/local/lib"' '-DSBIN_DIR="/usr/local/sbin"' -I. -I.. -D_REENTRANT -D__EXTENSIONS__ -D_FILE_OFFSET_BITS=64 -D_LARGEFILE_SOURCE -D_LARGE_FILES -g -O2 -Wall -W -Wshadow -pedantic -std=gnu99 -MT mod_simple_vhost.lo -MD -MP -MF .deps/mod_simple_vhost.Tpo -c mod_simple_vhost.c -fPIC -DPIC -o .libs/mod_simple_vhost.o

# eid=1224
export LANG=C

$CC -shared -fPIC -DPIC .libs/mod_simple_vhost.o -g -O2 -Wl,-soname -Wl,mod_simple_vhost.so -o .libs/mod_simple_vhost.so

# eid=1266
export LANG=en_US.UTF-8

$CC -DHAVE_CONFIG_H -DHAVE_VERSION_H '-DLIBRARY_DIR="/usr/local/lib"' '-DSBIN_DIR="/usr/local/sbin"' -I. -I.. -D_REENTRANT -D__EXTENSIONS__ -D_FILE_OFFSET_BITS=64 -D_LARGEFILE_SOURCE -D_LARGE_FILES -g -O2 -Wall -W -Wshadow -pedantic -std=gnu99 -MT mod_fastcgi.lo -MD -MP -MF .deps/mod_fastcgi.Tpo -c mod_fastcgi.c -fPIC -DPIC -o .libs/mod_fastcgi.o

# eid=1283
export LANG=C

$CC -shared -fPIC -DPIC .libs/mod_fastcgi.o -g -O2 -Wl,-soname -Wl,mod_fastcgi.so -o .libs/mod_fastcgi.so

# eid=1325
export LANG=en_US.UTF-8

$CC -DHAVE_CONFIG_H -DHAVE_VERSION_H '-DLIBRARY_DIR="/usr/local/lib"' '-DSBIN_DIR="/usr/local/sbin"' -I. -I.. -D_REENTRANT -D__EXTENSIONS__ -D_FILE_OFFSET_BITS=64 -D_LARGEFILE_SOURCE -D_LARGE_FILES -g -O2 -Wall -W -Wshadow -pedantic -std=gnu99 -MT mod_extforward.lo -MD -MP -MF .deps/mod_extforward.Tpo -c mod_extforward.c -fPIC -DPIC -o .libs/mod_extforward.o

# eid=1342
export LANG=C

$CC -shared -fPIC -DPIC .libs/mod_extforward.o -g -O2 -Wl,-soname -Wl,mod_extforward.so -o .libs/mod_extforward.so

# eid=1384
export LANG=en_US.UTF-8

$CC -DHAVE_CONFIG_H -DHAVE_VERSION_H '-DLIBRARY_DIR="/usr/local/lib"' '-DSBIN_DIR="/usr/local/sbin"' -I. -I.. -D_REENTRANT -D__EXTENSIONS__ -D_FILE_OFFSET_BITS=64 -D_LARGEFILE_SOURCE -D_LARGE_FILES -g -O2 -Wall -W -Wshadow -pedantic -std=gnu99 -MT mod_access.lo -MD -MP -MF .deps/mod_access.Tpo -c mod_access.c -fPIC -DPIC -o .libs/mod_access.o

# eid=1401
export LANG=C

$CC -shared -fPIC -DPIC .libs/mod_access.o -g -O2 -Wl,-soname -Wl,mod_access.so -o .libs/mod_access.so

# eid=1443
export LANG=en_US.UTF-8

$CC -DHAVE_CONFIG_H -DHAVE_VERSION_H '-DLIBRARY_DIR="/usr/local/lib"' '-DSBIN_DIR="/usr/local/sbin"' -I. -I.. -D_REENTRANT -D__EXTENSIONS__ -D_FILE_OFFSET_BITS=64 -D_LARGEFILE_SOURCE -D_LARGE_FILES -g -O2 -Wall -W -Wshadow -pedantic -std=gnu99 -MT mod_compress.lo -MD -MP -MF .deps/mod_compress.Tpo -c mod_compress.c -fPIC -DPIC -o .libs/mod_compress.o

# eid=1460
export LANG=C

$CC -shared -fPIC -DPIC .libs/mod_compress.o -lz -g -O2 -Wl,-soname -Wl,mod_compress.so -o .libs/mod_compress.so

# eid=1502
export LANG=en_US.UTF-8

$CC -DHAVE_CONFIG_H -DHAVE_VERSION_H '-DLIBRARY_DIR="/usr/local/lib"' '-DSBIN_DIR="/usr/local/sbin"' -I. -I.. -D_REENTRANT -D__EXTENSIONS__ -D_FILE_OFFSET_BITS=64 -D_LARGEFILE_SOURCE -D_LARGE_FILES -g -O2 -Wall -W -Wshadow -pedantic -std=gnu99 -MT mod_deflate.lo -MD -MP -MF .deps/mod_deflate.Tpo -c mod_deflate.c -fPIC -DPIC -o .libs/mod_deflate.o

# eid=1519
export LANG=C

$CC -shared -fPIC -DPIC .libs/mod_deflate.o -lz -g -O2 -Wl,-soname -Wl,mod_deflate.so -o .libs/mod_deflate.so

# eid=1561
export LANG=en_US.UTF-8

$CC -DHAVE_CONFIG_H -DHAVE_VERSION_H '-DLIBRARY_DIR="/usr/local/lib"' '-DSBIN_DIR="/usr/local/sbin"' -I. -I.. -D_REENTRANT -D__EXTENSIONS__ -D_FILE_OFFSET_BITS=64 -D_LARGEFILE_SOURCE -D_LARGE_FILES -g -O2 -Wall -W -Wshadow -pedantic -std=gnu99 -MT mod_auth.lo -MD -MP -MF .deps/mod_auth.Tpo -c mod_auth.c -fPIC -DPIC -o .libs/mod_auth.o

# eid=1578
export LANG=C

$CC -shared -fPIC -DPIC .libs/mod_auth.o -g -O2 -Wl,-soname -Wl,mod_auth.so -o .libs/mod_auth.so

# eid=1620
export LANG=en_US.UTF-8

$CC -DHAVE_CONFIG_H -DHAVE_VERSION_H '-DLIBRARY_DIR="/usr/local/lib"' '-DSBIN_DIR="/usr/local/sbin"' -I. -I.. -D_REENTRANT -D__EXTENSIONS__ -D_FILE_OFFSET_BITS=64 -D_LARGEFILE_SOURCE -D_LARGE_FILES -g -O2 -Wall -W -Wshadow -pedantic -std=gnu99 -MT mod_authn_file.lo -MD -MP -MF .deps/mod_authn_file.Tpo -c mod_authn_file.c -fPIC -DPIC -o .libs/mod_authn_file.o

# eid=1637
export LANG=C

$CC -shared -fPIC -DPIC .libs/mod_authn_file.o -lcrypt -g -O2 -Wl,-soname -Wl,mod_authn_file.so -o .libs/mod_authn_file.so

# eid=1679
export LANG=en_US.UTF-8

$CC -DHAVE_CONFIG_H -DHAVE_VERSION_H '-DLIBRARY_DIR="/usr/local/lib"' '-DSBIN_DIR="/usr/local/sbin"' -I. -I.. -D_REENTRANT -D__EXTENSIONS__ -D_FILE_OFFSET_BITS=64 -D_LARGEFILE_SOURCE -D_LARGE_FILES -g -O2 -Wall -W -Wshadow -pedantic -std=gnu99 -MT mod_rewrite.lo -MD -MP -MF .deps/mod_rewrite.Tpo -c mod_rewrite.c -fPIC -DPIC -o .libs/mod_rewrite.o

# eid=1696
export LANG=C

$CC -shared -fPIC -DPIC .libs/mod_rewrite.o -lpcre -g -O2 -Wl,-soname -Wl,mod_rewrite.so -o .libs/mod_rewrite.so

# eid=1738
export LANG=en_US.UTF-8

$CC -DHAVE_CONFIG_H -DHAVE_VERSION_H '-DLIBRARY_DIR="/usr/local/lib"' '-DSBIN_DIR="/usr/local/sbin"' -I. -I.. -D_REENTRANT -D__EXTENSIONS__ -D_FILE_OFFSET_BITS=64 -D_LARGEFILE_SOURCE -D_LARGE_FILES -g -O2 -Wall -W -Wshadow -pedantic -std=gnu99 -MT mod_redirect.lo -MD -MP -MF .deps/mod_redirect.Tpo -c mod_redirect.c -fPIC -DPIC -o .libs/mod_redirect.o

# eid=1755
export LANG=C

$CC -shared -fPIC -DPIC .libs/mod_redirect.o -lpcre -g -O2 -Wl,-soname -Wl,mod_redirect.so -o .libs/mod_redirect.so

# eid=1797
export LANG=en_US.UTF-8

$CC -DHAVE_CONFIG_H -DHAVE_VERSION_H '-DLIBRARY_DIR="/usr/local/lib"' '-DSBIN_DIR="/usr/local/sbin"' -I. -I.. -D_REENTRANT -D__EXTENSIONS__ -D_FILE_OFFSET_BITS=64 -D_LARGEFILE_SOURCE -D_LARGE_FILES -g -O2 -Wall -W -Wshadow -pedantic -std=gnu99 -MT mod_status.lo -MD -MP -MF .deps/mod_status.Tpo -c mod_status.c -fPIC -DPIC -o .libs/mod_status.o

# eid=1814
export LANG=C

$CC -shared -fPIC -DPIC .libs/mod_status.o -g -O2 -Wl,-soname -Wl,mod_status.so -o .libs/mod_status.so

# eid=1856
export LANG=en_US.UTF-8

$CC -DHAVE_CONFIG_H -DHAVE_VERSION_H '-DLIBRARY_DIR="/usr/local/lib"' '-DSBIN_DIR="/usr/local/sbin"' -I. -I.. -D_REENTRANT -D__EXTENSIONS__ -D_FILE_OFFSET_BITS=64 -D_LARGEFILE_SOURCE -D_LARGE_FILES -g -O2 -Wall -W -Wshadow -pedantic -std=gnu99 -MT mod_accesslog.lo -MD -MP -MF .deps/mod_accesslog.Tpo -c mod_accesslog.c -fPIC -DPIC -o .libs/mod_accesslog.o

# eid=1873
export LANG=C

$CC -shared -fPIC -DPIC .libs/mod_accesslog.o -g -O2 -Wl,-soname -Wl,mod_accesslog.so -o .libs/mod_accesslog.so

# eid=1915
export LANG=en_US.UTF-8

$CC -DHAVE_CONFIG_H -DHAVE_VERSION_H '-DLIBRARY_DIR="/usr/local/lib"' '-DSBIN_DIR="/usr/local/sbin"' -I. -I.. -D_REENTRANT -D__EXTENSIONS__ -D_FILE_OFFSET_BITS=64 -D_LARGEFILE_SOURCE -D_LARGE_FILES -g -O2 -Wall -W -Wshadow -pedantic -std=gnu99 -MT mod_uploadprogress.lo -MD -MP -MF .deps/mod_uploadprogress.Tpo -c mod_uploadprogress.c -fPIC -DPIC -o .libs/mod_uploadprogress.o

# eid=1932
export LANG=C

$CC -shared -fPIC -DPIC .libs/mod_uploadprogress.o -g -O2 -Wl,-soname -Wl,mod_uploadprogress.so -o .libs/mod_uploadprogress.so

# eid=1942
export LANG=en_US.UTF-8
export SHLVL=5
unset DUALCASE

$CC -DHAVE_CONFIG_H -DHAVE_VERSION_H '-DLIBRARY_DIR="/usr/local/lib"' '-DSBIN_DIR="/usr/local/sbin"' -I. -I.. -DDEBUG_PROC_OPEN -D_REENTRANT -D__EXTENSIONS__ -D_FILE_OFFSET_BITS=64 -D_LARGEFILE_SOURCE -D_LARGE_FILES -g -O2 -Wall -W -Wshadow -pedantic -std=gnu99 -MT proc_open-proc_open.o -MD -MP -MF .deps/proc_open-proc_open.Tpo -c -o proc_open-proc_open.o proc_open.c

# eid=1948
$CC -DHAVE_CONFIG_H -DHAVE_VERSION_H '-DLIBRARY_DIR="/usr/local/lib"' '-DSBIN_DIR="/usr/local/sbin"' -I. -I.. -DDEBUG_PROC_OPEN -D_REENTRANT -D__EXTENSIONS__ -D_FILE_OFFSET_BITS=64 -D_LARGEFILE_SOURCE -D_LARGE_FILES -g -O2 -Wall -W -Wshadow -pedantic -std=gnu99 -MT proc_open-buffer.o -MD -MP -MF .deps/proc_open-buffer.Tpo -c -o proc_open-buffer.o buffer.c

# eid=1965
export DUALCASE=1
export LANG=C
export SHLVL=6

$CC -g -O2 -Wall -W -Wshadow -pedantic -std=gnu99 -o proc_open proc_open-proc_open.o proc_open-buffer.o

# eid=1969
export LANG=en_US.UTF-8
export SHLVL=5
unset DUALCASE

$CC -DHAVE_CONFIG_H -DHAVE_VERSION_H '-DLIBRARY_DIR="/usr/local/lib"' '-DSBIN_DIR="/usr/local/sbin"' -I. -I.. -D_REENTRANT -D__EXTENSIONS__ -D_FILE_OFFSET_BITS=64 -D_LARGEFILE_SOURCE -D_LARGE_FILES -g -O2 -Wall -W -Wshadow -pedantic -std=gnu99 -MT test_buffer.o -MD -MP -MF .deps/test_buffer.Tpo -c -o test_buffer.o test_buffer.c

# eid=1975
$CC -DHAVE_CONFIG_H -DHAVE_VERSION_H '-DLIBRARY_DIR="/usr/local/lib"' '-DSBIN_DIR="/usr/local/sbin"' -I. -I.. -D_REENTRANT -D__EXTENSIONS__ -D_FILE_OFFSET_BITS=64 -D_LARGEFILE_SOURCE -D_LARGE_FILES -g -O2 -Wall -W -Wshadow -pedantic -std=gnu99 -MT buffer.o -MD -MP -MF .deps/buffer.Tpo -c -o buffer.o buffer.c

# eid=1992
export DUALCASE=1
export LANG=C
export SHLVL=6

$CC -g -O2 -Wall -W -Wshadow -pedantic -std=gnu99 -o test_buffer test_buffer.o buffer.o

# eid=1996
export LANG=en_US.UTF-8
export SHLVL=5
unset DUALCASE

$CC -DHAVE_CONFIG_H -DHAVE_VERSION_H '-DLIBRARY_DIR="/usr/local/lib"' '-DSBIN_DIR="/usr/local/sbin"' -I. -I.. -D_REENTRANT -D__EXTENSIONS__ -D_FILE_OFFSET_BITS=64 -D_LARGEFILE_SOURCE -D_LARGE_FILES -g -O2 -Wall -W -Wshadow -pedantic -std=gnu99 -MT test_base64.o -MD -MP -MF .deps/test_base64.Tpo -c -o test_base64.o test_base64.c

# eid=2002
$CC -DHAVE_CONFIG_H -DHAVE_VERSION_H '-DLIBRARY_DIR="/usr/local/lib"' '-DSBIN_DIR="/usr/local/sbin"' -I. -I.. -D_REENTRANT -D__EXTENSIONS__ -D_FILE_OFFSET_BITS=64 -D_LARGEFILE_SOURCE -D_LARGE_FILES -g -O2 -Wall -W -Wshadow -pedantic -std=gnu99 -MT base64.o -MD -MP -MF .deps/base64.Tpo -c -o base64.o base64.c

# eid=2019
export DUALCASE=1
export LANG=C
export SHLVL=6

$CC -g -O2 -Wall -W -Wshadow -pedantic -std=gnu99 -o test_base64 test_base64.o base64.o buffer.o

# eid=2023
export LANG=en_US.UTF-8
export SHLVL=5
unset DUALCASE

$CC -DHAVE_CONFIG_H -DHAVE_VERSION_H '-DLIBRARY_DIR="/usr/local/lib"' '-DSBIN_DIR="/usr/local/sbin"' -I. -I.. -D_REENTRANT -D__EXTENSIONS__ -D_FILE_OFFSET_BITS=64 -D_LARGEFILE_SOURCE -D_LARGE_FILES -g -O2 -Wall -W -Wshadow -pedantic -std=gnu99 -MT test_configfile.o -MD -MP -MF .deps/test_configfile.Tpo -c -o test_configfile.o test_configfile.c

# eid=2029
$CC -DHAVE_CONFIG_H -DHAVE_VERSION_H '-DLIBRARY_DIR="/usr/local/lib"' '-DSBIN_DIR="/usr/local/sbin"' -I. -I.. -D_REENTRANT -D__EXTENSIONS__ -D_FILE_OFFSET_BITS=64 -D_LARGEFILE_SOURCE -D_LARGE_FILES -g -O2 -Wall -W -Wshadow -pedantic -std=gnu99 -MT array.o -MD -MP -MF .deps/array.Tpo -c -o array.o array.c

# eid=2035
$CC -DHAVE_CONFIG_H -DHAVE_VERSION_H '-DLIBRARY_DIR="/usr/local/lib"' '-DSBIN_DIR="/usr/local/sbin"' -I. -I.. -D_REENTRANT -D__EXTENSIONS__ -D_FILE_OFFSET_BITS=64 -D_LARGEFILE_SOURCE -D_LARGE_FILES -g -O2 -Wall -W -Wshadow -pedantic -std=gnu99 -MT data_string.o -MD -MP -MF .deps/data_string.Tpo -c -o data_string.o data_string.c

# eid=2041
$CC -DHAVE_CONFIG_H -DHAVE_VERSION_H '-DLIBRARY_DIR="/usr/local/lib"' '-DSBIN_DIR="/usr/local/sbin"' -I. -I.. -D_REENTRANT -D__EXTENSIONS__ -D_FILE_OFFSET_BITS=64 -D_LARGEFILE_SOURCE -D_LARGE_FILES -g -O2 -Wall -W -Wshadow -pedantic -std=gnu99 -MT keyvalue.o -MD -MP -MF .deps/keyvalue.Tpo -c -o keyvalue.o keyvalue.c

# eid=2047
$CC -DHAVE_CONFIG_H -DHAVE_VERSION_H '-DLIBRARY_DIR="/usr/local/lib"' '-DSBIN_DIR="/usr/local/sbin"' -I. -I.. -D_REENTRANT -D__EXTENSIONS__ -D_FILE_OFFSET_BITS=64 -D_LARGEFILE_SOURCE -D_LARGE_FILES -g -O2 -Wall -W -Wshadow -pedantic -std=gnu99 -MT vector.o -MD -MP -MF .deps/vector.Tpo -c -o vector.o vector.c

# eid=2053
$CC -DHAVE_CONFIG_H -DHAVE_VERSION_H '-DLIBRARY_DIR="/usr/local/lib"' '-DSBIN_DIR="/usr/local/sbin"' -I. -I.. -D_REENTRANT -D__EXTENSIONS__ -D_FILE_OFFSET_BITS=64 -D_LARGEFILE_SOURCE -D_LARGE_FILES -g -O2 -Wall -W -Wshadow -pedantic -std=gnu99 -MT log.o -MD -MP -MF .deps/log.Tpo -c -o log.o log.c

# eid=2070
export DUALCASE=1
export LANG=C
export SHLVL=6

$CC -g -O2 -Wall -W -Wshadow -pedantic -std=gnu99 -o test_configfile test_configfile.o buffer.o array.o data_string.o keyvalue.o vector.o log.o -lpcre

# eid=2074
export LANG=en_US.UTF-8
export SHLVL=5
unset DUALCASE

$CC -DHAVE_CONFIG_H -DHAVE_VERSION_H '-DLIBRARY_DIR="/usr/local/lib"' '-DSBIN_DIR="/usr/local/sbin"' -I. -I.. -D_REENTRANT -D__EXTENSIONS__ -D_FILE_OFFSET_BITS=64 -D_LARGEFILE_SOURCE -D_LARGE_FILES -g -O2 -Wall -W -Wshadow -pedantic -std=gnu99 -MT lighttpd-server.o -MD -MP -MF .deps/lighttpd-server.Tpo -c -o lighttpd-server.o server.c

# eid=2080
$CC -DHAVE_CONFIG_H -DHAVE_VERSION_H '-DLIBRARY_DIR="/usr/local/lib"' '-DSBIN_DIR="/usr/local/sbin"' -I. -I.. -D_REENTRANT -D__EXTENSIONS__ -D_FILE_OFFSET_BITS=64 -D_LARGEFILE_SOURCE -D_LARGE_FILES -g -O2 -Wall -W -Wshadow -pedantic -std=gnu99 -MT lighttpd-response.o -MD -MP -MF .deps/lighttpd-response.Tpo -c -o lighttpd-response.o response.c

# eid=2086
$CC -DHAVE_CONFIG_H -DHAVE_VERSION_H '-DLIBRARY_DIR="/usr/local/lib"' '-DSBIN_DIR="/usr/local/sbin"' -I. -I.. -D_REENTRANT -D__EXTENSIONS__ -D_FILE_OFFSET_BITS=64 -D_LARGEFILE_SOURCE -D_LARGE_FILES -g -O2 -Wall -W -Wshadow -pedantic -std=gnu99 -MT lighttpd-connections.o -MD -MP -MF .deps/lighttpd-connections.Tpo -c -o lighttpd-connections.o connections.c

# eid=2092
$CC -DHAVE_CONFIG_H -DHAVE_VERSION_H '-DLIBRARY_DIR="/usr/local/lib"' '-DSBIN_DIR="/usr/local/sbin"' -I. -I.. -D_REENTRANT -D__EXTENSIONS__ -D_FILE_OFFSET_BITS=64 -D_LARGEFILE_SOURCE -D_LARGE_FILES -g -O2 -Wall -W -Wshadow -pedantic -std=gnu99 -MT lighttpd-network.o -MD -MP -MF .deps/lighttpd-network.Tpo -c -o lighttpd-network.o network.c

# eid=2098
$CC -DHAVE_CONFIG_H -DHAVE_VERSION_H '-DLIBRARY_DIR="/usr/local/lib"' '-DSBIN_DIR="/usr/local/sbin"' -I. -I.. -D_REENTRANT -D__EXTENSIONS__ -D_FILE_OFFSET_BITS=64 -D_LARGEFILE_SOURCE -D_LARGE_FILES -g -O2 -Wall -W -Wshadow -pedantic -std=gnu99 -MT lighttpd-network_write.o -MD -MP -MF .deps/lighttpd-network_write.Tpo -c -o lighttpd-network_write.o network_write.c

# eid=2104
$CC -DHAVE_CONFIG_H -DHAVE_VERSION_H '-DLIBRARY_DIR="/usr/local/lib"' '-DSBIN_DIR="/usr/local/sbin"' -I. -I.. -D_REENTRANT -D__EXTENSIONS__ -D_FILE_OFFSET_BITS=64 -D_LARGEFILE_SOURCE -D_LARGE_FILES -g -O2 -Wall -W -Wshadow -pedantic -std=gnu99 -MT lighttpd-network_linux_sendfile.o -MD -MP -MF .deps/lighttpd-network_linux_sendfile.Tpo -c -o lighttpd-network_linux_sendfile.o network_linux_sendfile.c

# eid=2110
$CC -DHAVE_CONFIG_H -DHAVE_VERSION_H '-DLIBRARY_DIR="/usr/local/lib"' '-DSBIN_DIR="/usr/local/sbin"' -I. -I.. -D_REENTRANT -D__EXTENSIONS__ -D_FILE_OFFSET_BITS=64 -D_LARGEFILE_SOURCE -D_LARGE_FILES -g -O2 -Wall -W -Wshadow -pedantic -std=gnu99 -MT lighttpd-network_write_mmap.o -MD -MP -MF .deps/lighttpd-network_write_mmap.Tpo -c -o lighttpd-network_write_mmap.o network_write_mmap.c

# eid=2116
$CC -DHAVE_CONFIG_H -DHAVE_VERSION_H '-DLIBRARY_DIR="/usr/local/lib"' '-DSBIN_DIR="/usr/local/sbin"' -I. -I.. -D_REENTRANT -D__EXTENSIONS__ -D_FILE_OFFSET_BITS=64 -D_LARGEFILE_SOURCE -D_LARGE_FILES -g -O2 -Wall -W -Wshadow -pedantic -std=gnu99 -MT lighttpd-network_write_no_mmap.o -MD -MP -MF .deps/lighttpd-network_write_no_mmap.Tpo -c -o lighttpd-network_write_no_mmap.o network_write_no_mmap.c

# eid=2122
$CC -DHAVE_CONFIG_H -DHAVE_VERSION_H '-DLIBRARY_DIR="/usr/local/lib"' '-DSBIN_DIR="/usr/local/sbin"' -I. -I.. -D_REENTRANT -D__EXTENSIONS__ -D_FILE_OFFSET_BITS=64 -D_LARGEFILE_SOURCE -D_LARGE_FILES -g -O2 -Wall -W -Wshadow -pedantic -std=gnu99 -MT lighttpd-network_freebsd_sendfile.o -MD -MP -MF .deps/lighttpd-network_freebsd_sendfile.Tpo -c -o lighttpd-network_freebsd_sendfile.o network_freebsd_sendfile.c

# eid=2128
$CC -DHAVE_CONFIG_H -DHAVE_VERSION_H '-DLIBRARY_DIR="/usr/local/lib"' '-DSBIN_DIR="/usr/local/sbin"' -I. -I.. -D_REENTRANT -D__EXTENSIONS__ -D_FILE_OFFSET_BITS=64 -D_LARGEFILE_SOURCE -D_LARGE_FILES -g -O2 -Wall -W -Wshadow -pedantic -std=gnu99 -MT lighttpd-network_writev.o -MD -MP -MF .deps/lighttpd-network_writev.Tpo -c -o lighttpd-network_writev.o network_writev.c

# eid=2134
$CC -DHAVE_CONFIG_H -DHAVE_VERSION_H '-DLIBRARY_DIR="/usr/local/lib"' '-DSBIN_DIR="/usr/local/sbin"' -I. -I.. -D_REENTRANT -D__EXTENSIONS__ -D_FILE_OFFSET_BITS=64 -D_LARGEFILE_SOURCE -D_LARGE_FILES -g -O2 -Wall -W -Wshadow -pedantic -std=gnu99 -MT lighttpd-network_solaris_sendfilev.o -MD -MP -MF .deps/lighttpd-network_solaris_sendfilev.Tpo -c -o lighttpd-network_solaris_sendfilev.o network_solaris_sendfilev.c

# eid=2140
$CC -DHAVE_CONFIG_H -DHAVE_VERSION_H '-DLIBRARY_DIR="/usr/local/lib"' '-DSBIN_DIR="/usr/local/sbin"' -I. -I.. -D_REENTRANT -D__EXTENSIONS__ -D_FILE_OFFSET_BITS=64 -D_LARGEFILE_SOURCE -D_LARGE_FILES -g -O2 -Wall -W -Wshadow -pedantic -std=gnu99 -MT lighttpd-network_openssl.o -MD -MP -MF .deps/lighttpd-network_openssl.Tpo -c -o lighttpd-network_openssl.o network_openssl.c

# eid=2146
$CC -DHAVE_CONFIG_H -DHAVE_VERSION_H '-DLIBRARY_DIR="/usr/local/lib"' '-DSBIN_DIR="/usr/local/sbin"' -I. -I.. -D_REENTRANT -D__EXTENSIONS__ -D_FILE_OFFSET_BITS=64 -D_LARGEFILE_SOURCE -D_LARGE_FILES -g -O2 -Wall -W -Wshadow -pedantic -std=gnu99 -MT lighttpd-network_darwin_sendfile.o -MD -MP -MF .deps/lighttpd-network_darwin_sendfile.Tpo -c -o lighttpd-network_darwin_sendfile.o network_darwin_sendfile.c

# eid=2152
$CC -DHAVE_CONFIG_H -DHAVE_VERSION_H '-DLIBRARY_DIR="/usr/local/lib"' '-DSBIN_DIR="/usr/local/sbin"' -I. -I.. -D_REENTRANT -D__EXTENSIONS__ -D_FILE_OFFSET_BITS=64 -D_LARGEFILE_SOURCE -D_LARGE_FILES -g -O2 -Wall -W -Wshadow -pedantic -std=gnu99 -MT lighttpd-configfile.o -MD -MP -MF .deps/lighttpd-configfile.Tpo -c -o lighttpd-configfile.o configfile.c

# eid=2158
$CC -DHAVE_CONFIG_H -DHAVE_VERSION_H '-DLIBRARY_DIR="/usr/local/lib"' '-DSBIN_DIR="/usr/local/sbin"' -I. -I.. -D_REENTRANT -D__EXTENSIONS__ -D_FILE_OFFSET_BITS=64 -D_LARGEFILE_SOURCE -D_LARGE_FILES -g -O2 -Wall -W -Wshadow -pedantic -std=gnu99 -MT lighttpd-configparser.o -MD -MP -MF .deps/lighttpd-configparser.Tpo -c -o lighttpd-configparser.o configparser.c

# eid=2164
$CC -DHAVE_CONFIG_H -DHAVE_VERSION_H '-DLIBRARY_DIR="/usr/local/lib"' '-DSBIN_DIR="/usr/local/sbin"' -I. -I.. -D_REENTRANT -D__EXTENSIONS__ -D_FILE_OFFSET_BITS=64 -D_LARGEFILE_SOURCE -D_LARGE_FILES -g -O2 -Wall -W -Wshadow -pedantic -std=gnu99 -MT lighttpd-request.o -MD -MP -MF .deps/lighttpd-request.Tpo -c -o lighttpd-request.o request.c

# eid=2170
$CC -DHAVE_CONFIG_H -DHAVE_VERSION_H '-DLIBRARY_DIR="/usr/local/lib"' '-DSBIN_DIR="/usr/local/sbin"' -I. -I.. -D_REENTRANT -D__EXTENSIONS__ -D_FILE_OFFSET_BITS=64 -D_LARGEFILE_SOURCE -D_LARGE_FILES -g -O2 -Wall -W -Wshadow -pedantic -std=gnu99 -MT lighttpd-proc_open.o -MD -MP -MF .deps/lighttpd-proc_open.Tpo -c -o lighttpd-proc_open.o proc_open.c

# eid=2176
$CC -DHAVE_CONFIG_H -DHAVE_VERSION_H '-DLIBRARY_DIR="/usr/local/lib"' '-DSBIN_DIR="/usr/local/sbin"' -I. -I.. -D_REENTRANT -D__EXTENSIONS__ -D_FILE_OFFSET_BITS=64 -D_LARGEFILE_SOURCE -D_LARGE_FILES -g -O2 -Wall -W -Wshadow -pedantic -std=gnu99 -MT lighttpd-base64.o -MD -MP -MF .deps/lighttpd-base64.Tpo -c -o lighttpd-base64.o base64.c

# eid=2182
$CC -DHAVE_CONFIG_H -DHAVE_VERSION_H '-DLIBRARY_DIR="/usr/local/lib"' '-DSBIN_DIR="/usr/local/sbin"' -I. -I.. -D_REENTRANT -D__EXTENSIONS__ -D_FILE_OFFSET_BITS=64 -D_LARGEFILE_SOURCE -D_LARGE_FILES -g -O2 -Wall -W -Wshadow -pedantic -std=gnu99 -MT lighttpd-buffer.o -MD -MP -MF .deps/lighttpd-buffer.Tpo -c -o lighttpd-buffer.o buffer.c

# eid=2188
$CC -DHAVE_CONFIG_H -DHAVE_VERSION_H '-DLIBRARY_DIR="/usr/local/lib"' '-DSBIN_DIR="/usr/local/sbin"' -I. -I.. -D_REENTRANT -D__EXTENSIONS__ -D_FILE_OFFSET_BITS=64 -D_LARGEFILE_SOURCE -D_LARGE_FILES -g -O2 -Wall -W -Wshadow -pedantic -std=gnu99 -MT lighttpd-log.o -MD -MP -MF .deps/lighttpd-log.Tpo -c -o lighttpd-log.o log.c

# eid=2194
$CC -DHAVE_CONFIG_H -DHAVE_VERSION_H '-DLIBRARY_DIR="/usr/local/lib"' '-DSBIN_DIR="/usr/local/sbin"' -I. -I.. -D_REENTRANT -D__EXTENSIONS__ -D_FILE_OFFSET_BITS=64 -D_LARGEFILE_SOURCE -D_LARGE_FILES -g -O2 -Wall -W -Wshadow -pedantic -std=gnu99 -MT lighttpd-keyvalue.o -MD -MP -MF .deps/lighttpd-keyvalue.Tpo -c -o lighttpd-keyvalue.o keyvalue.c

# eid=2200
$CC -DHAVE_CONFIG_H -DHAVE_VERSION_H '-DLIBRARY_DIR="/usr/local/lib"' '-DSBIN_DIR="/usr/local/sbin"' -I. -I.. -D_REENTRANT -D__EXTENSIONS__ -D_FILE_OFFSET_BITS=64 -D_LARGEFILE_SOURCE -D_LARGE_FILES -g -O2 -Wall -W -Wshadow -pedantic -std=gnu99 -MT lighttpd-chunk.o -MD -MP -MF .deps/lighttpd-chunk.Tpo -c -o lighttpd-chunk.o chunk.c

# eid=2206
$CC -DHAVE_CONFIG_H -DHAVE_VERSION_H '-DLIBRARY_DIR="/usr/local/lib"' '-DSBIN_DIR="/usr/local/sbin"' -I. -I.. -D_REENTRANT -D__EXTENSIONS__ -D_FILE_OFFSET_BITS=64 -D_LARGEFILE_SOURCE -D_LARGE_FILES -g -O2 -Wall -W -Wshadow -pedantic -std=gnu99 -MT lighttpd-http_chunk.o -MD -MP -MF .deps/lighttpd-http_chunk.Tpo -c -o lighttpd-http_chunk.o http_chunk.c

# eid=2212
$CC -DHAVE_CONFIG_H -DHAVE_VERSION_H '-DLIBRARY_DIR="/usr/local/lib"' '-DSBIN_DIR="/usr/local/sbin"' -I. -I.. -D_REENTRANT -D__EXTENSIONS__ -D_FILE_OFFSET_BITS=64 -D_LARGEFILE_SOURCE -D_LARGE_FILES -g -O2 -Wall -W -Wshadow -pedantic -std=gnu99 -MT lighttpd-stream.o -MD -MP -MF .deps/lighttpd-stream.Tpo -c -o lighttpd-stream.o stream.c

# eid=2218
$CC -DHAVE_CONFIG_H -DHAVE_VERSION_H '-DLIBRARY_DIR="/usr/local/lib"' '-DSBIN_DIR="/usr/local/sbin"' -I. -I.. -D_REENTRANT -D__EXTENSIONS__ -D_FILE_OFFSET_BITS=64 -D_LARGEFILE_SOURCE -D_LARGE_FILES -g -O2 -Wall -W -Wshadow -pedantic -std=gnu99 -MT lighttpd-fdevent.o -MD -MP -MF .deps/lighttpd-fdevent.Tpo -c -o lighttpd-fdevent.o fdevent.c

# eid=2224
$CC -DHAVE_CONFIG_H -DHAVE_VERSION_H '-DLIBRARY_DIR="/usr/local/lib"' '-DSBIN_DIR="/usr/local/sbin"' -I. -I.. -D_REENTRANT -D__EXTENSIONS__ -D_FILE_OFFSET_BITS=64 -D_LARGEFILE_SOURCE -D_LARGE_FILES -g -O2 -Wall -W -Wshadow -pedantic -std=gnu99 -MT lighttpd-stat_cache.o -MD -MP -MF .deps/lighttpd-stat_cache.Tpo -c -o lighttpd-stat_cache.o stat_cache.c

# eid=2230
$CC -DHAVE_CONFIG_H -DHAVE_VERSION_H '-DLIBRARY_DIR="/usr/local/lib"' '-DSBIN_DIR="/usr/local/sbin"' -I. -I.. -D_REENTRANT -D__EXTENSIONS__ -D_FILE_OFFSET_BITS=64 -D_LARGEFILE_SOURCE -D_LARGE_FILES -g -O2 -Wall -W -Wshadow -pedantic -std=gnu99 -MT lighttpd-plugin.o -MD -MP -MF .deps/lighttpd-plugin.Tpo -c -o lighttpd-plugin.o plugin.c

# eid=2236
$CC -DHAVE_CONFIG_H -DHAVE_VERSION_H '-DLIBRARY_DIR="/usr/local/lib"' '-DSBIN_DIR="/usr/local/sbin"' -I. -I.. -D_REENTRANT -D__EXTENSIONS__ -D_FILE_OFFSET_BITS=64 -D_LARGEFILE_SOURCE -D_LARGE_FILES -g -O2 -Wall -W -Wshadow -pedantic -std=gnu99 -MT lighttpd-joblist.o -MD -MP -MF .deps/lighttpd-joblist.Tpo -c -o lighttpd-joblist.o joblist.c

# eid=2242
$CC -DHAVE_CONFIG_H -DHAVE_VERSION_H '-DLIBRARY_DIR="/usr/local/lib"' '-DSBIN_DIR="/usr/local/sbin"' -I. -I.. -D_REENTRANT -D__EXTENSIONS__ -D_FILE_OFFSET_BITS=64 -D_LARGEFILE_SOURCE -D_LARGE_FILES -g -O2 -Wall -W -Wshadow -pedantic -std=gnu99 -MT lighttpd-etag.o -MD -MP -MF .deps/lighttpd-etag.Tpo -c -o lighttpd-etag.o etag.c

# eid=2248
$CC -DHAVE_CONFIG_H -DHAVE_VERSION_H '-DLIBRARY_DIR="/usr/local/lib"' '-DSBIN_DIR="/usr/local/sbin"' -I. -I.. -D_REENTRANT -D__EXTENSIONS__ -D_FILE_OFFSET_BITS=64 -D_LARGEFILE_SOURCE -D_LARGE_FILES -g -O2 -Wall -W -Wshadow -pedantic -std=gnu99 -MT lighttpd-array.o -MD -MP -MF .deps/lighttpd-array.Tpo -c -o lighttpd-array.o array.c

# eid=2254
$CC -DHAVE_CONFIG_H -DHAVE_VERSION_H '-DLIBRARY_DIR="/usr/local/lib"' '-DSBIN_DIR="/usr/local/sbin"' -I. -I.. -D_REENTRANT -D__EXTENSIONS__ -D_FILE_OFFSET_BITS=64 -D_LARGEFILE_SOURCE -D_LARGE_FILES -g -O2 -Wall -W -Wshadow -pedantic -std=gnu99 -MT lighttpd-data_string.o -MD -MP -MF .deps/lighttpd-data_string.Tpo -c -o lighttpd-data_string.o data_string.c

# eid=2260
$CC -DHAVE_CONFIG_H -DHAVE_VERSION_H '-DLIBRARY_DIR="/usr/local/lib"' '-DSBIN_DIR="/usr/local/sbin"' -I. -I.. -D_REENTRANT -D__EXTENSIONS__ -D_FILE_OFFSET_BITS=64 -D_LARGEFILE_SOURCE -D_LARGE_FILES -g -O2 -Wall -W -Wshadow -pedantic -std=gnu99 -MT lighttpd-data_array.o -MD -MP -MF .deps/lighttpd-data_array.Tpo -c -o lighttpd-data_array.o data_array.c

# eid=2266
$CC -DHAVE_CONFIG_H -DHAVE_VERSION_H '-DLIBRARY_DIR="/usr/local/lib"' '-DSBIN_DIR="/usr/local/sbin"' -I. -I.. -D_REENTRANT -D__EXTENSIONS__ -D_FILE_OFFSET_BITS=64 -D_LARGEFILE_SOURCE -D_LARGE_FILES -g -O2 -Wall -W -Wshadow -pedantic -std=gnu99 -MT lighttpd-data_integer.o -MD -MP -MF .deps/lighttpd-data_integer.Tpo -c -o lighttpd-data_integer.o data_integer.c

# eid=2272
$CC -DHAVE_CONFIG_H -DHAVE_VERSION_H '-DLIBRARY_DIR="/usr/local/lib"' '-DSBIN_DIR="/usr/local/sbin"' -I. -I.. -D_REENTRANT -D__EXTENSIONS__ -D_FILE_OFFSET_BITS=64 -D_LARGEFILE_SOURCE -D_LARGE_FILES -g -O2 -Wall -W -Wshadow -pedantic -std=gnu99 -MT lighttpd-md5.o -MD -MP -MF .deps/lighttpd-md5.Tpo -c -o lighttpd-md5.o md5.c

# eid=2278
$CC -DHAVE_CONFIG_H -DHAVE_VERSION_H '-DLIBRARY_DIR="/usr/local/lib"' '-DSBIN_DIR="/usr/local/sbin"' -I. -I.. -D_REENTRANT -D__EXTENSIONS__ -D_FILE_OFFSET_BITS=64 -D_LARGEFILE_SOURCE -D_LARGE_FILES -g -O2 -Wall -W -Wshadow -pedantic -std=gnu99 -MT lighttpd-data_fastcgi.o -MD -MP -MF .deps/lighttpd-data_fastcgi.Tpo -c -o lighttpd-data_fastcgi.o data_fastcgi.c

# eid=2284
$CC -DHAVE_CONFIG_H -DHAVE_VERSION_H '-DLIBRARY_DIR="/usr/local/lib"' '-DSBIN_DIR="/usr/local/sbin"' -I. -I.. -D_REENTRANT -D__EXTENSIONS__ -D_FILE_OFFSET_BITS=64 -D_LARGEFILE_SOURCE -D_LARGE_FILES -g -O2 -Wall -W -Wshadow -pedantic -std=gnu99 -MT lighttpd-vector.o -MD -MP -MF .deps/lighttpd-vector.Tpo -c -o lighttpd-vector.o vector.c

# eid=2290
$CC -DHAVE_CONFIG_H -DHAVE_VERSION_H '-DLIBRARY_DIR="/usr/local/lib"' '-DSBIN_DIR="/usr/local/sbin"' -I. -I.. -D_REENTRANT -D__EXTENSIONS__ -D_FILE_OFFSET_BITS=64 -D_LARGEFILE_SOURCE -D_LARGE_FILES -g -O2 -Wall -W -Wshadow -pedantic -std=gnu99 -MT lighttpd-fdevent_select.o -MD -MP -MF .deps/lighttpd-fdevent_select.Tpo -c -o lighttpd-fdevent_select.o fdevent_select.c

# eid=2296
$CC -DHAVE_CONFIG_H -DHAVE_VERSION_H '-DLIBRARY_DIR="/usr/local/lib"' '-DSBIN_DIR="/usr/local/sbin"' -I. -I.. -D_REENTRANT -D__EXTENSIONS__ -D_FILE_OFFSET_BITS=64 -D_LARGEFILE_SOURCE -D_LARGE_FILES -g -O2 -Wall -W -Wshadow -pedantic -std=gnu99 -MT lighttpd-fdevent_libev.o -MD -MP -MF .deps/lighttpd-fdevent_libev.Tpo -c -o lighttpd-fdevent_libev.o fdevent_libev.c

# eid=2302
$CC -DHAVE_CONFIG_H -DHAVE_VERSION_H '-DLIBRARY_DIR="/usr/local/lib"' '-DSBIN_DIR="/usr/local/sbin"' -I. -I.. -D_REENTRANT -D__EXTENSIONS__ -D_FILE_OFFSET_BITS=64 -D_LARGEFILE_SOURCE -D_LARGE_FILES -g -O2 -Wall -W -Wshadow -pedantic -std=gnu99 -MT lighttpd-fdevent_poll.o -MD -MP -MF .deps/lighttpd-fdevent_poll.Tpo -c -o lighttpd-fdevent_poll.o fdevent_poll.c

# eid=2308
$CC -DHAVE_CONFIG_H -DHAVE_VERSION_H '-DLIBRARY_DIR="/usr/local/lib"' '-DSBIN_DIR="/usr/local/sbin"' -I. -I.. -D_REENTRANT -D__EXTENSIONS__ -D_FILE_OFFSET_BITS=64 -D_LARGEFILE_SOURCE -D_LARGE_FILES -g -O2 -Wall -W -Wshadow -pedantic -std=gnu99 -MT lighttpd-fdevent_linux_sysepoll.o -MD -MP -MF .deps/lighttpd-fdevent_linux_sysepoll.Tpo -c -o lighttpd-fdevent_linux_sysepoll.o fdevent_linux_sysepoll.c

# eid=2314
$CC -DHAVE_CONFIG_H -DHAVE_VERSION_H '-DLIBRARY_DIR="/usr/local/lib"' '-DSBIN_DIR="/usr/local/sbin"' -I. -I.. -D_REENTRANT -D__EXTENSIONS__ -D_FILE_OFFSET_BITS=64 -D_LARGEFILE_SOURCE -D_LARGE_FILES -g -O2 -Wall -W -Wshadow -pedantic -std=gnu99 -MT lighttpd-fdevent_solaris_devpoll.o -MD -MP -MF .deps/lighttpd-fdevent_solaris_devpoll.Tpo -c -o lighttpd-fdevent_solaris_devpoll.o fdevent_solaris_devpoll.c

# eid=2320
$CC -DHAVE_CONFIG_H -DHAVE_VERSION_H '-DLIBRARY_DIR="/usr/local/lib"' '-DSBIN_DIR="/usr/local/sbin"' -I. -I.. -D_REENTRANT -D__EXTENSIONS__ -D_FILE_OFFSET_BITS=64 -D_LARGEFILE_SOURCE -D_LARGE_FILES -g -O2 -Wall -W -Wshadow -pedantic -std=gnu99 -MT lighttpd-fdevent_solaris_port.o -MD -MP -MF .deps/lighttpd-fdevent_solaris_port.Tpo -c -o lighttpd-fdevent_solaris_port.o fdevent_solaris_port.c

# eid=2326
$CC -DHAVE_CONFIG_H -DHAVE_VERSION_H '-DLIBRARY_DIR="/usr/local/lib"' '-DSBIN_DIR="/usr/local/sbin"' -I. -I.. -D_REENTRANT -D__EXTENSIONS__ -D_FILE_OFFSET_BITS=64 -D_LARGEFILE_SOURCE -D_LARGE_FILES -g -O2 -Wall -W -Wshadow -pedantic -std=gnu99 -MT lighttpd-fdevent_freebsd_kqueue.o -MD -MP -MF .deps/lighttpd-fdevent_freebsd_kqueue.Tpo -c -o lighttpd-fdevent_freebsd_kqueue.o fdevent_freebsd_kqueue.c

# eid=2332
$CC -DHAVE_CONFIG_H -DHAVE_VERSION_H '-DLIBRARY_DIR="/usr/local/lib"' '-DSBIN_DIR="/usr/local/sbin"' -I. -I.. -D_REENTRANT -D__EXTENSIONS__ -D_FILE_OFFSET_BITS=64 -D_LARGEFILE_SOURCE -D_LARGE_FILES -g -O2 -Wall -W -Wshadow -pedantic -std=gnu99 -MT lighttpd-data_config.o -MD -MP -MF .deps/lighttpd-data_config.Tpo -c -o lighttpd-data_config.o data_config.c

# eid=2338
$CC -DHAVE_CONFIG_H -DHAVE_VERSION_H '-DLIBRARY_DIR="/usr/local/lib"' '-DSBIN_DIR="/usr/local/sbin"' -I. -I.. -D_REENTRANT -D__EXTENSIONS__ -D_FILE_OFFSET_BITS=64 -D_LARGEFILE_SOURCE -D_LARGE_FILES -g -O2 -Wall -W -Wshadow -pedantic -std=gnu99 -MT lighttpd-inet_ntop_cache.o -MD -MP -MF .deps/lighttpd-inet_ntop_cache.Tpo -c -o lighttpd-inet_ntop_cache.o inet_ntop_cache.c

# eid=2344
$CC -DHAVE_CONFIG_H -DHAVE_VERSION_H '-DLIBRARY_DIR="/usr/local/lib"' '-DSBIN_DIR="/usr/local/sbin"' -I. -I.. -D_REENTRANT -D__EXTENSIONS__ -D_FILE_OFFSET_BITS=64 -D_LARGEFILE_SOURCE -D_LARGE_FILES -g -O2 -Wall -W -Wshadow -pedantic -std=gnu99 -MT lighttpd-crc32.o -MD -MP -MF .deps/lighttpd-crc32.Tpo -c -o lighttpd-crc32.o crc32.c

# eid=2350
$CC -DHAVE_CONFIG_H -DHAVE_VERSION_H '-DLIBRARY_DIR="/usr/local/lib"' '-DSBIN_DIR="/usr/local/sbin"' -I. -I.. -D_REENTRANT -D__EXTENSIONS__ -D_FILE_OFFSET_BITS=64 -D_LARGEFILE_SOURCE -D_LARGE_FILES -g -O2 -Wall -W -Wshadow -pedantic -std=gnu99 -MT lighttpd-connections-glue.o -MD -MP -MF .deps/lighttpd-connections-glue.Tpo -c -o lighttpd-connections-glue.o connections-glue.c

# eid=2356
$CC -DHAVE_CONFIG_H -DHAVE_VERSION_H '-DLIBRARY_DIR="/usr/local/lib"' '-DSBIN_DIR="/usr/local/sbin"' -I. -I.. -D_REENTRANT -D__EXTENSIONS__ -D_FILE_OFFSET_BITS=64 -D_LARGEFILE_SOURCE -D_LARGE_FILES -g -O2 -Wall -W -Wshadow -pedantic -std=gnu99 -MT lighttpd-configfile-glue.o -MD -MP -MF .deps/lighttpd-configfile-glue.Tpo -c -o lighttpd-configfile-glue.o configfile-glue.c

# eid=2362
$CC -DHAVE_CONFIG_H -DHAVE_VERSION_H '-DLIBRARY_DIR="/usr/local/lib"' '-DSBIN_DIR="/usr/local/sbin"' -I. -I.. -D_REENTRANT -D__EXTENSIONS__ -D_FILE_OFFSET_BITS=64 -D_LARGEFILE_SOURCE -D_LARGE_FILES -g -O2 -Wall -W -Wshadow -pedantic -std=gnu99 -MT lighttpd-http-header-glue.o -MD -MP -MF .deps/lighttpd-http-header-glue.Tpo -c -o lighttpd-http-header-glue.o http-header-glue.c

# eid=2368
$CC -DHAVE_CONFIG_H -DHAVE_VERSION_H '-DLIBRARY_DIR="/usr/local/lib"' '-DSBIN_DIR="/usr/local/sbin"' -I. -I.. -D_REENTRANT -D__EXTENSIONS__ -D_FILE_OFFSET_BITS=64 -D_LARGEFILE_SOURCE -D_LARGE_FILES -g -O2 -Wall -W -Wshadow -pedantic -std=gnu99 -MT lighttpd-http_auth.o -MD -MP -MF .deps/lighttpd-http_auth.Tpo -c -o lighttpd-http_auth.o http_auth.c

# eid=2374
$CC -DHAVE_CONFIG_H -DHAVE_VERSION_H '-DLIBRARY_DIR="/usr/local/lib"' '-DSBIN_DIR="/usr/local/sbin"' -I. -I.. -D_REENTRANT -D__EXTENSIONS__ -D_FILE_OFFSET_BITS=64 -D_LARGEFILE_SOURCE -D_LARGE_FILES -g -O2 -Wall -W -Wshadow -pedantic -std=gnu99 -MT lighttpd-rand.o -MD -MP -MF .deps/lighttpd-rand.Tpo -c -o lighttpd-rand.o rand.c

# eid=2380
$CC -DHAVE_CONFIG_H -DHAVE_VERSION_H '-DLIBRARY_DIR="/usr/local/lib"' '-DSBIN_DIR="/usr/local/sbin"' -I. -I.. -D_REENTRANT -D__EXTENSIONS__ -D_FILE_OFFSET_BITS=64 -D_LARGEFILE_SOURCE -D_LARGE_FILES -g -O2 -Wall -W -Wshadow -pedantic -std=gnu99 -MT lighttpd-splaytree.o -MD -MP -MF .deps/lighttpd-splaytree.Tpo -c -o lighttpd-splaytree.o splaytree.c

# eid=2386
$CC -DHAVE_CONFIG_H -DHAVE_VERSION_H '-DLIBRARY_DIR="/usr/local/lib"' '-DSBIN_DIR="/usr/local/sbin"' -I. -I.. -D_REENTRANT -D__EXTENSIONS__ -D_FILE_OFFSET_BITS=64 -D_LARGEFILE_SOURCE -D_LARGE_FILES -g -O2 -Wall -W -Wshadow -pedantic -std=gnu99 -MT lighttpd-status_counter.o -MD -MP -MF .deps/lighttpd-status_counter.Tpo -c -o lighttpd-status_counter.o status_counter.c

# eid=2392
$CC -DHAVE_CONFIG_H -DHAVE_VERSION_H '-DLIBRARY_DIR="/usr/local/lib"' '-DSBIN_DIR="/usr/local/sbin"' -I. -I.. -D_REENTRANT -D__EXTENSIONS__ -D_FILE_OFFSET_BITS=64 -D_LARGEFILE_SOURCE -D_LARGE_FILES -g -O2 -Wall -W -Wshadow -pedantic -std=gnu99 -MT lighttpd-safe_memclear.o -MD -MP -MF .deps/lighttpd-safe_memclear.Tpo -c -o lighttpd-safe_memclear.o safe_memclear.c

# eid=2409
export DUALCASE=1
export LANG=C
export SHLVL=6

$CC -g -O2 -Wall -W -Wshadow -pedantic -std=gnu99 -o lighttpd lighttpd-server.o lighttpd-response.o lighttpd-connections.o lighttpd-network.o lighttpd-network_write.o lighttpd-network_linux_sendfile.o lighttpd-network_write_mmap.o lighttpd-network_write_no_mmap.o lighttpd-network_freebsd_sendfile.o lighttpd-network_writev.o lighttpd-network_solaris_sendfilev.o lighttpd-network_openssl.o lighttpd-network_darwin_sendfile.o lighttpd-configfile.o lighttpd-configparser.o lighttpd-request.o lighttpd-proc_open.o lighttpd-base64.o lighttpd-buffer.o lighttpd-log.o lighttpd-keyvalue.o lighttpd-chunk.o lighttpd-http_chunk.o lighttpd-stream.o lighttpd-fdevent.o lighttpd-stat_cache.o lighttpd-plugin.o lighttpd-joblist.o lighttpd-etag.o lighttpd-array.o lighttpd-data_string.o lighttpd-data_array.o lighttpd-data_integer.o lighttpd-md5.o lighttpd-data_fastcgi.o lighttpd-vector.o lighttpd-fdevent_select.o lighttpd-fdevent_libev.o lighttpd-fdevent_poll.o lighttpd-fdevent_linux_sysepoll.o lighttpd-fdevent_solaris_devpoll.o lighttpd-fdevent_solaris_port.o lighttpd-fdevent_freebsd_kqueue.o lighttpd-data_config.o lighttpd-inet_ntop_cache.o lighttpd-crc32.o lighttpd-connections-glue.o lighttpd-configfile-glue.o lighttpd-http-header-glue.o lighttpd-http_auth.o lighttpd-rand.o lighttpd-splaytree.o lighttpd-status_counter.o lighttpd-safe_memclear.o -Wl,--export-dynamic -lpcre -ldl

# eid=2413
export LANG=en_US.UTF-8
export SHLVL=5
unset DUALCASE

$CC -DHAVE_CONFIG_H -DHAVE_VERSION_H '-DLIBRARY_DIR="/usr/local/lib"' '-DSBIN_DIR="/usr/local/sbin"' -I. -I.. -D_REENTRANT -D__EXTENSIONS__ -D_FILE_OFFSET_BITS=64 -D_LARGEFILE_SOURCE -D_LARGE_FILES -g -O2 -Wall -W -Wshadow -pedantic -std=gnu99 -MT lighttpd-angel.o -MD -MP -MF .deps/lighttpd-angel.Tpo -c -o lighttpd-angel.o lighttpd-angel.c

# eid=2430
export DUALCASE=1
export LANG=C
export SHLVL=6

$CC -g -O2 -Wall -W -Wshadow -pedantic -std=gnu99 -o lighttpd-angel lighttpd-angel.o
