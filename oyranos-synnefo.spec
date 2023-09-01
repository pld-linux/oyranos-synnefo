Summary:	Synnefo - Qt color management front-end
Summary(pl.UTF-8):	Synnefo - graficzny interfejs Qt do zarządzania kolorami
Name:		oyranos-synnefo
Version:	1.1.0
Release:	1
License:	BSD
Group:		Applications
#Source0Download: https://github.com/oyranos-cms/Synnefo/releases
Source0:	https://github.com/oyranos-cms/Synnefo/archive/%{version}/Synnefo-%{version}.tar.gz
# Source0-md5:	1b15008e1ac639a6f353ba0b43fa3ad3
URL:		https://github.com/oyranos-cms/Synnefo
BuildRequires:	Qt5DBus-devel >= 5
BuildRequires:	Qt5Widgets-devel >= 5
BuildRequires:	cmake >= 2.4
BuildRequires:	oyranos-devel
BuildRequires:	qt5-build >= 5
BuildRequires:	rpmbuild(macros) >= 1.605
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Synnefo is a Qt color management front-end. It uses the Oyranos CMS to
provide the ability to set and examine device profiles, as well as to
change system-wide color settings.

%description -l pl.UTF-8
Synnefo to graficzny interfejs Qt do zarządzania kolorami.
Wykorzystuje system zarządzania kolorami (CMS) Oyranos do ustawiania i
sprawdzania profili urządzeń, a także zmiany systemowych ustawień
kolorów.

%package devel
Summary:	Header files for Oyranos Synnefo library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki Oyranos Synnefo
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	Qt5DBus-devel >= 5
Requires:	Qt5Widgets-devel >= 5
Requires:	oyranos-devel

%description devel
Header files for Oyranos Synnefo library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki Oyranos Synnefo.

%package static
Summary:	Static Oyranos Synnefo library
Summary(pl.UTF-8):	Statyczna biblioteka Oyranos Synnefo
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static Oyranos Synnefo library.

%description static -l pl.UTF-8
Statyczna biblioteka Oyranos Synnefo.

%prep
%setup -q -n Synnefo-%{version}

%build
install -d build
cd build
%cmake .. \
	-DINSTALL_LIB_DIR=%{_libdir}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS.md COPYING.md README.md
%attr(755,root,root) %{_bindir}/oyranos-config-synnefo
%attr(755,root,root) %{_libdir}/libOyranosSynnefo.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libOyranosSynnefo.so.1
%{_desktopdir}/oyranos-config-synnefo.desktop
%{_pixmapsdir}/oyranos-config-synnefo.png
%{_pixmapsdir}/oyranos-config-synnefo.svg
%{_mandir}/man1/oyranos-config-synnefo.1*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libOyranosSynnefo.so
%{_includedir}/synnefo
%{_libdir}/cmake/synnefo

%files static
%defattr(644,root,root,755)
%{_libdir}/libOyranosSynnefo-static.a
