%define api	0.2
%define major	0
%define libname	%mklibname %{name} %{api} %{major}
%define devname	%mklibname -d %{name}
%define girname	%mklibname %{name}-gir %{api}

Summary:	Map rendering application and library
Name:		memphis
Version:	0.2.3
Release:	9
License:	LGPLv2+
Group:		System/Libraries
Url:		https://trac.openstreetmap.ch/trac/memphis/
Source0:	http://wenner.ch/files/public/mirror/memphis/%{name}-%{version}.tar.gz
BuildRequires:	pkgconfig(cairo)
BuildRequires:	pkgconfig(expat)
BuildRequires:	pkgconfig(glib-2.0)
BuildRequires:	pkgconfig(gobject-introspection-1.0)

%description
Memphis is a map-rendering application and a library for OpenStreetMap
written in C using eXpat, Cairo and GLib.

Features:
 * Parsing of nodes and ways from a OSM XML export file.
 * XML file format to define drawing rules.
 * Dynamic adaptable drawing rules.
 * Cairo rendering engine.
 * GObject based API. 

%package data
Summary:	Data files for %{name}
Group:		System/Libraries
BuildArch:	noarch
Obsoletes:	%{name} < 0.2.3-7

%description data
The data files for %{name}.

%package -n %{libname}
Summary:	Map rendering library
Group:		System/Libraries
Requires:	%{name}-data = %{version}-%{release}

%description -n %{libname}
Libmemphis is a map-rendering library for OpenStreetMap
written in C using eXpat, Cairo and GLib.

Features:
 * Parsing of nodes and ways from a OSM XML export file.
 * XML file format to define drawing rules.
 * Dynamic adaptable drawing rules.
 * Cairo rendering engine.
 * GObject based API. 

%package -n %{devname}
Summary:	Map rendering library
Group:		Development/C
Requires:	%{libname} = %{version}-%{release}
Requires:	%{girname} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}

%description -n %{devname}
This package includes the development files for %{name}. 

%package -n %{girname}
Summary:	GObject Introspection interface description for %{name}
Group:		System/Libraries

%description -n %{girname}
GObject Introspection interface description for %{name}.

%prep
%setup -q
%apply_patches

%build
%configure2_5x --disable-static
%make

%install
%makeinstall_std

%files data
%{_datadir}/%{name}

%files -n %{libname}
%{_libdir}/lib%{name}-%{api}.so.%{major}*

%files -n %{girname}
%{_libdir}/girepository-1.0/Memphis-%{api}.typelib

%files -n %{devname}
%doc README AUTHORS ChangeLog
%doc %{_datadir}/gtk-doc/html/lib%{name}
%{_libdir}/lib%{name}-%{api}.so
%{_includedir}/lib%{name}-%{api}/
%{_libdir}/pkgconfig/%{name}-%{api}.pc
%{_datadir}/gir-1.0/Memphis-%{api}.gir

