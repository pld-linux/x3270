%define		fversion	%(echo %{version} |tr -d .)
%define		mversion	%(echo %{version} |cut -f -2 -d .)
Summary:	An X Window System based IBM 3278/3279 terminal emulator
Summary(de.UTF-8):	X-basierter 3270-Emulator
Summary(fr.UTF-8):	Emulateur 3270 pour X
Summary(pl.UTF-8):	Emulator terminala IBM 3278/3279 pod X Window System
Summary(ru.UTF-8):	Эмулятор терминала IBM 3278/3279 для X Window
Summary(tr.UTF-8):	X tabanlı 3270 öykünümcüsü
Summary(uk.UTF-8):	Емулятор терміналу IBM 3278/3279 для X Window
Summary(zh_CN.UTF-8):	一个基于 X 窗口系统的 IBM 3278/3279 终端模拟器。
Name:		x3270
Version:	3.3.4p4
Release:	3
License:	MIT
Group:		X11/Applications
Source0:	http://x3270.bgp.nu/download/%{name}-%{fversion}.tgz
# Source0-md5:	b90409b190380489f75fea231e8af2d8
Source1:	%{name}.desktop
Patch0:		%{name}-cc.patch
URL:		http://x3270.bgp.nu/
BuildRequires:	XFree86
BuildRequires:	XFree86-devel
BuildRequires:	automake
BuildRequires:	icu
Requires(post,postun):	/usr/X11R6/bin/mkfontdir
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_appdefsdir	/usr/X11R6/lib/X11/app-defaults

%description
The x3270 program opens a window in the X Window System which emulates
the actual look of an IBM 3278/3279 terminal, commonly used with
mainframe applications. x3270 also allows you to telnet to an IBM host
from the x3270 window.

%description -l de.UTF-8
Dieses Programm emuliert ein IBM 3270-Terminal, das üblicherweise mit
Mainframe-Anwendungen in einem X-Fenster ausgeführt wird.

%description -l fr.UTF-8
Ce programme émule un terminal IBM 3270, couramment utilisé sous X
window avec les gros systèmes.

%description -l pl.UTF-8
Program x3270 otwiera okienko pod X, które emuluje właściwy wygląd
terminala IBM 3278/3279, używanego głównie z aplikacjami mainframe.
x3270 pozwala także zatelnetować się na maszynę IBM z okienka x3270.

%description -l ru.UTF-8
Программа x3270 открывает окно в X Window System, эмулирующее вид
терминала IBM 3278/3279, часто используемого в мейнфреймах, и
позволяющее "telnet-ится" на хосты IBM.

%description -l tr.UTF-8
Bu program IBM 3270 uçbirim öykünümü yapar. IBM 3270 öykünümü bazı
eski bilgisayar sistemlerine bağlanmak için gerekebilir.

%description -l uk.UTF-8
Програма x3270 відкриває вікно в X Window System, яке емулює вид
терміналу IBM 3278/3279, часто використовуваного в мейнфреймах, і
дозволяє "telnet-итися" на хости IBM.

%description -l zh_CN.UTF-8
x3270 程序为 X 窗口系统打开一个窗口，它模拟
被普遍使用在大型机器上的程序的 IBM 3278/3279
终端的外观。X3270 还允许您从 x3270 窗口上远程
登录到一个 IBM 主机上。

%prep
%setup -q -n %{name}-%{mversion}
%patch -P0 -p1

%build
cp -f /usr/share/automake/config.sub .
cp -f /usr/share/automake/config.sub pr3287
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_appdefsdir},%{_desktopdir},%{_mandir}/man5}

%{__make} -j1 install install.man \
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
%attr(755,root,root) %{_bindir}/x3270
%attr(755,root,root) %{_bindir}/x3270if
%attr(755,root,root) %{_bindir}/pr3287
%dir %{_sysconfdir}/x3270
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/x3270/ibm_hosts
%{_desktopdir}/%{name}.desktop
%{_appdefsdir}/X3270
%{_fontsdir}/misc/3270*.pcf.gz
%{_mandir}/man?/*
