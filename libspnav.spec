Summary:	A free, compatible alternative for 3Dconnexion's 3D input device drivers and SDK
Summary(pl.UTF-8):	-
Name:		libspnav
Version:	0.2.2
Release:	1
License:	BSD
Group:		Development
Source0:	http://downloads.sourceforge.net/spacenav/%{name}-%{version}.tar.gz
# Source0-md5:	b85a0f4ab711e2d4f73a40e2e371f5ae
Patch0:		%{name}-build_fix.patch
URL:		http://spacenav.sourceforge.net/
BuildRequires:	automake
BuildRequires:	xorg-lib-libX11-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A free, compatible alternative for 3Dconnexion's 3D input device
drivers and SDK.

%description -l pl.UTF-8
Darmowa alternatywa dla oprogramowania urządzeń wejściowych i SDK
firmy 3Dconnexion.

%package devel
Summary:	Header files for %{name} library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki %{name}
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for %{name} library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki %{name}.

%prep
%setup -q
%patch0 -p1

%build
%configure \
	--disable-opt

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_libdir}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_libdir}/libspnav.so.*.*
%attr(755,root,root) %ghost %{_libdir}/libspnav.so.0

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libspnav.so
%{_includedir}/spnav*.h
