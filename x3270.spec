%define		fversion	%(echo %{version} |tr -d .)
%define		mversion	%(echo %{version} |cut -f -2 -d .)
Summary:	An X Window System based IBM 3278/3279 terminal emulator
Summary(de):	X-basierter 3270-Emulator
Summary(fr):	Emulateur 3270 pour X
Summary(pl):	Emulator terminala IBM 3278/3279 pod X Window System
Summary(ru):	Эмулятор терминала IBM 3278/3279 для X Window
Summary(tr):	X tabanlЩ 3270 ЖykЭnЭmcЭsЭ
Summary(uk):	Емулятор терм╕налу IBM 3278/3279 для X Window
Summary(zh_CN):	р╩╦ЖдёдБ IBM 3278/3279 жу╤к╣д X ╢╟©зо╣мЁ.ё
Name:		x3270
Version:	3.3.4p4
Release:	1
License:	MIT
Group:		X11/Applications
Source0:	http://x3270.bgp.nu/download/%{name}-%{fversion}.tgz
# Source0-md5:	b90409b190380489f75fea231e8af2d8
Source1:	%{name}.desktop
URL:		http://x3270.bgp.nu/
BuildRequires:	automake
BuildRequires:	XFree86
BuildRequires:	XFree86-devel
Requires(post,postun):	/usr/X11R6/bin/mkfontdir
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_appdefsdir	/usr/X11R6/lib/X11/app-defaults

%description
The x3270 program opens a window in the X Window System which emulates
the actual look of an IBM 3278/3279 terminal, commonly used with
mainframe applications. x3270 also allows you to telnet to an IBM host
from the x3270 window.

%description -l de
Dieses Programm emuliert ein IBM 3270-Terminal, das Эblicherweise mit
Mainframe-Anwendungen in einem X-Fenster ausgefЭhrt wird.

%description -l fr
Ce programme Иmule un terminal IBM 3270, couramment utilisИ sous X
window avec les gros systХmes.

%description -l pl
Program x3270 otwiera okienko pod X, ktСre emuluje wЁa╤ciwy wygl╠d
terminala IBM 3278/3279, u©ywanego gЁСwnie z aplikacjami mainframe.
x3270 pozwala tak©e zatelnetowaФ siЙ na maszynЙ IBM z okienka x3270.

%description -l ru
Программа x3270 открывает окно в X Window System, эмулирующее вид
терминала IBM 3278/3279, часто используемого в мейнфреймах, и
позволяющее "telnet-ится" на хосты IBM.

%description -l tr
Bu program IBM 3270 uГbirim ЖykЭnЭmЭ yapar. IBM 3270 ЖykЭnЭmЭ bazЩ
eski bilgisayar sistemlerine baПlanmak iГin gerekebilir.

%description -l uk
Програма x3270 в╕дкрива╓ в╕кно в X Window System, яке емулю╓ вид
терм╕налу IBM 3278/3279, часто використовуваного в мейнфреймах, ╕
дозволя╓ "telnet-итися" на хости IBM.

%prep
%setup -q -n %{name}-%{mversion}

%build
cp -f /usr/share/automake/config.sub .
cp -f /usr/share/automake/config.sub pr3287
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_appdefsdir},%{_desktopdir},%{_mandir}/man5}

%{__make} install install.man \
	BINDIR=%{_bindir} \
	MANDIR=%{_mandir} \
	DESTDIR=$RPM_BUILD_ROOT

install X3270.xad $RPM_BUILD_ROOT%{_appdefsdir}/X3270

install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}

mv -f $RPM_BUILD_ROOT%{_mandir}/{x3270.1*,man1}

%clean
rm -rf $RPM_BUILD_ROOT

%post
/usr/X11R6/bin/mkfontdir %{_fontsdir}/misc

%postun
/usr/X11R6/bin/mkfontdir %{_fontsdir}/misc

%files
%defattr(644,root,root,755)
#%doc Docs/*
%attr(755,root,root) %{_bindir}/x3270
%attr(755,root,root) %{_bindir}/x3270if
%attr(755,root,root) %{_bindir}/pr3287
%dir %{_sysconfdir}/x3270
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/x3270/ibm_hosts
%{_desktopdir}/%{name}.desktop
%{_appdefsdir}/X3270
%{_fontsdir}/misc/3270*.pcf.gz
#%{_mandir}/man1/x3270.1*
%{_mandir}/man?/*
