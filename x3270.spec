Summary:	An X Window System based IBM 3278/3279 terminal emulator
Summary(pl):	Emulator terminala IBM 3278/3279 pod X Window System
Name:		x3270
Version:	3.1.1.6
Release:	7
License:	MIT
Group:		X11/Applications
Source0:	ftp://ftp.x.org/contrib/applications/%{name}-%{version}.tar.gz
Patch0:		%{name}-3.1.1.6-glibc.patch
Prereq:		/usr/X11R6/bin/mkfontdir
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man

%description
The x3270 program opens a window in the X Window System which emulates
the actual look of an IBM 3278/3279 terminal, commonly used with
mainframe applications. x3270 also allows you to telnet to an IBM host
from the x3270 window.

Install the x3270 package if you need to access IBM hosts using an IBM
3278/3279 terminal emulator.

%description -l pl
Program x3270 otwiera okienko pod X, które emuluje w³a¶ciwy wygl±d
terminala IBM 3278/3279, u¿ywanego g³ównie z aplikacjami mainframe.
x3270 pozwala tak¿e ztelnetowaæ siê na maszynê IBM z okienka x3270.

%prep
%setup -q -n x3270-3.1.1
%patch -p1

%build
xmkmf
%{__make} CXXDEBUGFLAGS="%{rpmcflags}" \
	CDEBUGFLAGS="%{rpmcflags}" \
	LIBX3270DIR=%{_datadir}/%{name}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_libdir}/X11/app-defaults
install -d $RPM_BUILD_ROOT%{_sysconfdir}/X11/wmconfig

%{__make} install install.man DESTDIR=$RPM_BUILD_ROOT \
	LIBX3270DIR=%{_datadir}/%{name} \
	MKFONTDIR=mkfontdir

install X3270.xad $RPM_BUILD_ROOT%{_libdir}/X11/app-defaults/X3270

gzip -9nf Docs/*

cat > $RPM_BUILD_ROOT%{_sysconfdir}/X11/wmconfig/x3270 <<EOF
x3270 name "x3270"
x3270 description "3270 Terminal Emulator"
x3270 group Networking
x3270 exec "x3270 &"
EOF

%clean
rm -rf $RPM_BUILD_ROOT

%post
/usr/X11R6/bin/mkfontdir %{_fontsdir}/misc

%postun
/usr/X11R6/bin/mkfontdir %{_fontsdir}/misc

%files
%defattr(644,root,root,755)
%doc Docs/*
%config %{_sysconfdir}/X11/wmconfig/x3270
%config %{_libdir}/X11/app-defaults/X3270
%dir	%{_datadir}/x3270
%config	%{_datadir}/x3270/ibm_hosts
%attr(755,root,root) %{_bindir}/x3270
%{_fontsdir}/misc/3270.pcf.gz
%{_fontsdir}/misc/3270b.pcf.gz
%{_fontsdir}/misc/3270-12.pcf.gz
%{_fontsdir}/misc/3270-12b.pcf.gz
%{_fontsdir}/misc/3270-20.pcf.gz
%{_fontsdir}/misc/3270-20b.pcf.gz
%{_fontsdir}/misc/3270d.pcf.gz
%{_fontsdir}/misc/3270h.pcf.gz
%{_fontsdir}/misc/3270gt8.pcf.gz
%{_fontsdir}/misc/3270gt12.pcf.gz
%{_fontsdir}/misc/3270gt12b.pcf.gz
%{_fontsdir}/misc/3270gt16.pcf.gz
%{_fontsdir}/misc/3270gt16b.pcf.gz
%{_fontsdir}/misc/3270gt24.pcf.gz
%{_fontsdir}/misc/3270gt24b.pcf.gz
%{_fontsdir}/misc/3270gt32.pcf.gz
%{_fontsdir}/misc/3270gt32b.pcf.gz
%{_mandir}/man1/x3270.1x*
%{_mandir}/man1/x3270-script.1x*
%{_mandir}/man1/ibm_hosts.1x*
