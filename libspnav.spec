Summary:	A free, compatible alternative for 3Dconnexion's 3D input device drivers and SDK
Summary(pl.UTF-8):	Wolnodostępne alternatywne sterowniki wejściowe i SDK do urządzeń 3Dconnexion
Name:		libspnav
Version:	1.2
Release:	2
License:	BSD
Group:		Libraries
Source0:	https://github.com/FreeSpacenav/libspnav/archive/v%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	e50166801e49fab9dba026ab3023d367
Patch0:		%{name}-build_fix.patch
URL:		https://github.com/FreeSpacenav/libspnav
BuildRequires:	xorg-lib-libX11-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A free, compatible alternative for 3Dconnexion's 3D input device
drivers and SDK.

%description -l pl.UTF-8
Wolnodostępna, kompatybilna z oryginałem alternatywa dla sterowników i
SDK do trójwymiarowych urządzeń wejściowych firmy 3Dconnexion.

%package devel
Summary:	Header files for %{name} library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki %{name}
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	xorg-lib-libX11-devel

%description devel
Header files for %{name} library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki %{name}.

%package static
Summary:	Static libspnav library
Summary(pl.UTF-8):	Statyczna biblioteka libspnav
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static libspnav library.

%description static -l pl.UTF-8
Statyczna biblioteka libspnav.

%prep
%setup -q
%patch -P0 -p1

%build
%configure \
	--disable-debug \
	--disable-opt

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_libdir}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc README.md
%attr(755,root,root) %{_libdir}/libspnav.so.*.*
%ghost %{_libdir}/libspnav.so.0

%files devel
%defattr(644,root,root,755)
%{_libdir}/libspnav.so
%{_includedir}/spnav*.h
%{_pkgconfigdir}/spnav.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libspnav.a
