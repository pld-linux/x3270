Summary: An X Window System based IBM 3278/3279 terminal emulator.
Name: x3270
Version: 3.1.1.6
Release: 7
Copyright: MIT
Group: User Interface/X
Source: ftp://ftp.x.org/contrib/applications/x3270/x3270-3.1.1.6.tar.gz
Patch: x3270-3.1.1.6-glibc.patch
Prereq:  /usr/X11R6/bin/mkfontdir
BuildRoot: /var/tmp/%{name}-root

%description
The x3270 program opens a window in the X Window System which emulates
the actual look of an IBM 3278/3279 terminal, commonly used with
mainframe applications.  x3270 also allows you to telnet to an IBM host
from the x3270 window.

Install the x3270 package if you need to access IBM hosts using an
IBM 3278/3279 terminal emulator.

%prep
%setup -q -n x3270-3.1.1
%patch -p1

%build
xmkmf
make

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/X11R6/lib/X11/app-defaults

make DESTDIR=$RPM_BUILD_ROOT install install.man
install -m644 X3270.xad $RPM_BUILD_ROOT/usr/X11R6/lib/X11/app-defaults/X3270

( cd $RPM_BUILD_ROOT
  mkdir -p etc/X11/wmconfig
  cat > ./etc/X11/wmconfig/x3270 <<EOF
x3270 name "x3270"
x3270 description "3270 Terminal Emulator"
x3270 group Networking
x3270 exec "x3270 &"
EOF
)

%clean
rm -rf $RPM_BUILD_ROOT

%post
/usr/X11R6/bin/mkfontdir /usr/X11R6/lib/X11/fonts/misc

%postun
/usr/X11R6/bin/mkfontdir /usr/X11R6/lib/X11/fonts/misc

%files
%defattr(-,root,root)
%doc Docs
/usr/X11R6/bin/x3270
/usr/X11R6/lib/X11/fonts/misc/3270.pcf.gz     
/usr/X11R6/lib/X11/fonts/misc/3270b.pcf.gz               
/usr/X11R6/lib/X11/fonts/misc/3270-12.pcf.gz  
/usr/X11R6/lib/X11/fonts/misc/3270-12b.pcf.gz
/usr/X11R6/lib/X11/fonts/misc/3270-20.pcf.gz  
/usr/X11R6/lib/X11/fonts/misc/3270-20b.pcf.gz                   
/usr/X11R6/lib/X11/fonts/misc/3270d.pcf.gz             
/usr/X11R6/lib/X11/fonts/misc/3270h.pcf.gz             
/usr/X11R6/lib/X11/fonts/misc/3270gt8.pcf.gz                   
/usr/X11R6/lib/X11/fonts/misc/3270gt12.pcf.gz 
/usr/X11R6/lib/X11/fonts/misc/3270gt12b.pcf.gz
/usr/X11R6/lib/X11/fonts/misc/3270gt16.pcf.gz 
/usr/X11R6/lib/X11/fonts/misc/3270gt16b.pcf.gz                  
/usr/X11R6/lib/X11/fonts/misc/3270gt24.pcf.gz
/usr/X11R6/lib/X11/fonts/misc/3270gt24b.pcf.gz                  
/usr/X11R6/lib/X11/fonts/misc/3270gt32.pcf.gz 
/usr/X11R6/lib/X11/fonts/misc/3270gt32b.pcf.gz
/usr/X11R6/man/man1/x3270.1x
/usr/X11R6/man/man1/x3270-script.1x
/usr/X11R6/man/man1/ibm_hosts.1x
%config /etc/X11/wmconfig/x3270
%config /usr/X11R6/lib/X11/app-defaults/X3270
%dir	/usr/X11R6/lib/X11/x3270
%config	/usr/X11R6/lib/X11/x3270/ibm_hosts
