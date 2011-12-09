%define api 0.2
%define major 0
%define libname %mklibname %{name} %api %major
%define develname %mklibname -d %{name}

Summary: Map rendering application and library
Name: memphis
Version: 0.2.3
Release: 5
License: LGPLv2+
Group: System/Libraries
Url: https://trac.openstreetmap.ch/trac/memphis/
Source0: http://wenner.ch/files/public/mirror/memphis/%{name}-%{version}.tar.gz

Buildrequires: gtk-doc
Buildrequires: expat-devel
Buildrequires: pkgconfig(cairo)
Buildrequires: pkgconfig(glib-2.0)
Buildrequires: pkgconfig(gobject-introspection-1.0)

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
Summary: Map rendering library
Group: System/Libraries
Requires: %{name} >= %{version}

%description -n %{libname}
Libmemphis is a map-rendering library for OpenStreetMap
written in C using eXpat, Cairo and GLib.

Features:
 * Parsing of nodes and ways from a OSM XML export file.
 * XML file format to define drawing rules.
 * Dynamic adaptable drawing rules.
 * Cairo rendering engine.
 * GObject based API. 

%package -n %{develname}
Summary: Map rendering library
Group: Development/C
Requires: %{libname} = %{version}-%{release}
Provides: %{name}-devel = %{version}-%{release}

%description -n %{develname}
Libmemphis is a map-rendering library for OpenStreetMap
written in C using eXpat, Cairo and GLib.

Features:
 * Parsing of nodes and ways from a OSM XML export file.
 * XML file format to define drawing rules.
 * Dynamic adaptable drawing rules.
 * Cairo rendering engine.
 * GObject based API. 

%prep
%setup -q
%apply_patches

%build
%configure2_5x \
	--disable-static

%make

%install
rm -rf %{buildroot}
%makeinstall_std
rm -f %{buildroot}%{_libdir}/lib*.la

%files
%{_datadir}/%{name}

%files -n %{libname}
%doc README AUTHORS ChangeLog
%{_libdir}/libmemphis-%api.so.%{major}*
%{_libdir}/girepository-1.0/Memphis-%api.typelib

%files -n %{develname}
%doc ChangeLog
%{_libdir}/libmemphis-%api.so
%{_includedir}/libmemphis-%api/
%{_libdir}/pkgconfig/memphis-%api.pc
%{_datadir}/gtk-doc/html/libmemphis
%{_datadir}/gir-1.0/Memphis-%api.gir

