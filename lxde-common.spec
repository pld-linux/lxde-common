Summary:	Default configuration for LXDE
Summary(pl.UTF-8):	Domyślna konfiguracja LXDE
Name:		lxde-common
Version:	0.99.2
Release:	1
License:	GPL v2+
Group:		X11/Applications
Source0:	https://downloads.sourceforge.net/lxde/%{name}-%{version}.tar.xz
# Source0-md5:	14a9d19c4576dc15d985453ccb8ca9f6
URL:		http://www.lxde.org/
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
Requires:	openbox
Requires:	xorg-app-xprop
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
lxde-common package provides a set of default configuration for LXDE.

%description -l pl.UTF-8
Pakiet lxde-common dostarcza zestaw domyślnej konfiguracji środowiska
LXDE.

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
# COPYING specifies different licenses/source of some components
%doc AUTHORS COPYING README
%dir /etc/xdg/lxpanel
%dir /etc/xdg/lxpanel/LXDE
%config(noreplace) %verify(not md5 mtime size) /etc/xdg/lxpanel/LXDE/config
%dir /etc/xdg/lxpanel/LXDE/panels
%config(noreplace) %verify(not md5 mtime size) /etc/xdg/lxpanel/LXDE/panels/panel
%dir /etc/xdg/lxsession
%dir /etc/xdg/lxsession/LXDE
%config(noreplace) %verify(not md5 mtime size) /etc/xdg/lxsession/LXDE/autostart
%config(noreplace) %verify(not md5 mtime size) /etc/xdg/lxsession/LXDE/desktop.conf
%config(noreplace) %verify(not md5 mtime size) /etc/xdg/pcmanfm/LXDE/pcmanfm.conf
%dir /etc/xdg/openbox/LXDE
%config(noreplace) %verify(not md5 mtime size) /etc/xdg/openbox/LXDE/menu.xml
%config(noreplace) %verify(not md5 mtime size) /etc/xdg/openbox/LXDE/rc.xml
%attr(755,root,root) %{_bindir}/lxde-logout
%attr(755,root,root) %{_bindir}/openbox-lxde
%attr(755,root,root) %{_bindir}/startlxde
%{_datadir}/lxde
%{_datadir}/xsessions/LXDE.desktop
%{_desktopdir}/lxde-logout.desktop
%{_desktopdir}/lxde-screenlock.desktop
%{_mandir}/man1/lxde-logout.1*
%{_mandir}/man1/openbox-lxde.1*
%{_mandir}/man1/startlxde.1*
