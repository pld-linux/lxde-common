Summary:	Default configuration for LXDE
Name:		lxde-common
Version:	0.5.0
Release:	1
License:	GPL v2
Group:		X11/Applications
Source0:	http://downloads.sourceforge.net/lxde/%{name}-%{version}.tar.gz
# Source0-md5:	23606ab3d6e1039386d62a4b68b4ffc6
URL:		http://www.lxde.org/
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

rm -rf $RPM_BUILD_ROOT%{_datadir}/locale/{frp,ur_PK}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS README
%{_sysconfdir}/xdg/lxsession
%attr(755,root,root) %{_bindir}/lxde-logout
%attr(755,root,root) %{_bindir}/openbox-lxde
%attr(755,root,root) %{_bindir}/startlxde
%{_datadir}/lxde
%{_datadir}/lxpanel
%{_mandir}/man1/lxde-logout*
%{_mandir}/man1/openbox-lxde*
%{_mandir}/man1/startlxde*
%{_datadir}/xsessions/LXDE.desktop
