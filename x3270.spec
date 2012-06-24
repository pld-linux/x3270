Summary:	An X Window System based IBM 3278/3279 terminal emulator
Summary(pl):	Emulator terminala IBM 3278/3279 pod X Window System
Name:		x3270
Version:	3.1.1.9
Release:	1
License:	MIT
Group:		X11/Applications
Source0:	ftp://ftp.x.org/contrib/applications/%{name}-%{version}.tgz
BuildRequires:	XFree86-devel
Requires(post,postun):	/usr/X11R6/bin/mkfontdir
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man

%description
The x3270 program opens a window in the X Window System which emulates
the actual look of an IBM 3278/3279 terminal, commonly used with
mainframe applications. x3270 also allows you to telnet to an IBM host
from the x3270 window.

%description -l pl
Program x3270 otwiera okienko pod X, kt�re emuluje w�a�ciwy wygl�d
terminala IBM 3278/3279, u�ywanego g��wnie z aplikacjami mainframe.
x3270 pozwala tak�e ztelnetowa� si� na maszyn� IBM z okienka x3270.

%prep
%setup -q -n x3270-3.1.1

%build
xmkmf
# "LIB" is misleading - LIBX3270DIR contains only ibm_hosts configuration file
%{__make} CXXDEBUGFLAGS="%{rpmcflags}" \
	CDEBUGFLAGS="%{rpmcflags}" \
	LIBX3270DIR=%{_sysconfdir}/%{name}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_libdir}/X11/app-defaults,%{_applnkdir}/Network,%{_mandir}/man5}

%{__make} install install.man \
	DESTDIR=$RPM_BUILD_ROOT \
	LIBX3270DIR=%{_sysconfdir}/%{name} \
	MKFONTDIR=mkfontdir

install X3270.xad $RPM_BUILD_ROOT%{_libdir}/X11/app-defaults/X3270

cat > $RPM_BUILD_ROOT%{_applnkdir}/Network/x3270.desktop <<EOF
[Desktop Entry]
Name=x3270
Type=Application
Comment=3270 Terminal Emulator
Comment[pl]=Emulator Terminala 3270
Exec=x3270
Terminal=false
EOF

mv -f $RPM_BUILD_ROOT%{_mandir}/man{1/ibm_hosts.1x,5/ibm_hosts.5x}

%clean
rm -rf $RPM_BUILD_ROOT

%post
/usr/X11R6/bin/mkfontdir %{_fontsdir}/misc

%postun
/usr/X11R6/bin/mkfontdir %{_fontsdir}/misc

%files
%defattr(644,root,root,755)
%doc Docs/*
%attr(755,root,root) %{_bindir}/x3270
%attr(755,root,root) %{_bindir}/x3270if
%dir %{_sysconfdir}/x3270
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/x3270/ibm_hosts
%{_applnkdir}/Network/x3270.desktop
%config %{_libdir}/X11/app-defaults/X3270
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
%{_mandir}/man1/x3270if.1x*
%{_mandir}/man1/x3270-script.1x*
%{_mandir}/man5/ibm_hosts.5x*
