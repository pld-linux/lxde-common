Summary:	Default configuration for LXDE
Name:		lxde-common
Version:	0.5.5
Release:	1
License:	GPL v2
Group:		X11/Applications
Source0:	http://downloads.sourceforge.net/lxde/%{name}-%{version}.tar.gz
# Source0-md5:	e51a6b2a815a89fda1f497b509465a97
URL:		http://www.lxde.org/
Requires:	openbox
Requires:	xorg-app-xprop
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
lxde-common package provides a set of default configuration for LXDE.

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
%doc AUTHORS README
%dir /etc/xdg/lxsession
%dir /etc/xdg/lxsession/LXDE
%config(noreplace) %verify(not md5 mtime size) /etc/xdg/lxsession/LXDE/autostart
%config(noreplace) %verify(not md5 mtime size) /etc/xdg/lxsession/LXDE/desktop.conf
%config(noreplace) %verify(not md5 mtime size) /etc/xdg/pcmanfm/LXDE/pcmanfm.conf
%attr(755,root,root) %{_bindir}/lxde-logout
%attr(755,root,root) %{_bindir}/openbox-lxde
%attr(755,root,root) %{_bindir}/startlxde
%{_datadir}/lxde
%{_datadir}/lxpanel
%{_mandir}/man1/lxde-logout*
%{_mandir}/man1/openbox-lxde*
%{_mandir}/man1/startlxde*
%{_datadir}/xsessions/LXDE.desktop
