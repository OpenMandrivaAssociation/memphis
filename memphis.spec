%define api		0.2
%define gir_major	0.2
%define major		0
%define libname		%mklibname %{name} %{api} %{major}
%define devname		%mklibname -d %{name}
%define girname		%mklibname %{name}-gir %{gir_major}

Summary:	Map rendering application and library
Name:		memphis
Version:	0.2.3
Release:	6
Source0:	http://wenner.ch/files/public/mirror/memphis/%{name}-%{version}.tar.gz
License:	LGPLv2+
Group:		System/Libraries
Url:		https://trac.openstreetmap.ch/trac/memphis/
BuildRequires:	pkgconfig(glib-2.0)
BuildRequires:	pkgconfig(cairo)
BuildRequires:	pkgconfig(gobject-introspection-1.0)
BuildRequires:	expat-devel

%description
Memphis is a map-rendering application and a library for OpenStreetMap
written in C using eXpat, Cairo and GLib.

Features:
 * Parsing of nodes and ways from a OSM XML export file.
 * XML file format to define drawing rules.
 * Dynamic adaptable drawing rules.
 * Cairo rendering engine.
 * GObject based API. 

%package -n %{libname}
Summary:	Map rendering library
Group:		System/Libraries
Requires:	%{name} = %{version}-%{release}

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
Provides:	%{name}-devel = %{version}-%{release}
Provides:	lib%{name}-devel = %{version}-%{release}

%description -n %{devname}
Libmemphis is a map-rendering library for OpenStreetMap
written in C using eXpat, Cairo and GLib.

Features:
 * Parsing of nodes and ways from a OSM XML export file.
 * XML file format to define drawing rules.
 * Dynamic adaptable drawing rules.
 * Cairo rendering engine.
 * GObject based API. 

%package -n %{girname}
Summary:        GObject Introspection interface description for %{name}
Group:          System/Libraries
Requires:       %{libname} = %{version}-%{release}

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

#we don't want these
rm -f %{buildroot}%{_libdir}/*.la


%files
%{_datadir}/%{name}

%files -n %{libname}
%doc README AUTHORS ChangeLog
%{_libdir}/lib%{name}-%{api}.so.%{major}*

%files -n %{girname}
%{_libdir}/girepository-1.0/Memphis-%{gir_major}.typelib

%files -n %{devname}
%doc ChangeLog
%doc %{_datadir}/gtk-doc/html/lib%{name}
%{_libdir}/lib%{name}-%{api}.so
%{_includedir}/lib%{name}-%{api}/
%{_libdir}/pkgconfig/%{name}-%{api}.pc
%{_datadir}/gir-1.0/Memphis-%{gir_major}.gir
