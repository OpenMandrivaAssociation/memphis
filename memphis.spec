%define name memphis
%define version 0.2.1
%define release %mkrel 1

%define api 0.2
%define major 0
%define libname %mklibname %name %api %major
%define develname %mklibname -d %name

Summary: Map rendering application and library
Name: %{name}
Version: %{version}
Release: %{release}
Source0: http://wenner.ch/files/public/mirror/memphis/%{name}-%{version}.tar.gz
License: LGPLv2+
Group: System/Libraries
Url: https://trac.openstreetmap.ch/trac/memphis/
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Buildrequires: glib2-devel
Buildrequires: libcairo-devel
Buildrequires: libexpat-devel
Buildrequires: gobject-introspection-devel
Buildrequires: gtk-doc

%description
Memphis is a map-rendering application and a library for OpenStreetMap
written in C using eXpat, Cairo and GLib.

Features:
 * Parsing of nodes and ways from a OSM XML export file.
 * XML file format to define drawing rules.
 * Dynamic adaptable drawing rules.
 * Cairo rendering engine.
 * GObject based API. 

%package -n %libname
Summary: Map rendering library
Group: System/Libraries

%description -n %libname
Libmemphis is a map-rendering library for OpenStreetMap
written in C using eXpat, Cairo and GLib.

Features:
 * Parsing of nodes and ways from a OSM XML export file.
 * XML file format to define drawing rules.
 * Dynamic adaptable drawing rules.
 * Cairo rendering engine.
 * GObject based API. 

%package -n %develname
Summary: Map rendering library
Group: Development/C
Requires: %libname = %version-%release
Provides: %name-devel = %version-%release
Provides: lib%name-devel = %version-%release

%description -n %develname
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
# libtoolize --install --force
# aclocal
# autoconf
# automake

%build
%configure2_5x
%make

%install
rm -rf %{buildroot}
%makeinstall_std
rm -f %buildroot%_libdir/lib*.a

%clean
rm -rf %{buildroot}

%files -n %libname
%defattr(-,root,root)
%doc README AUTHORS ChangeLog
%_libdir/libmemphis-%api.so.%{major}*
%_libdir/girepository-1.0/Memphis-%api.typelib

%files -n %develname
%defattr(-,root,root)
%doc ChangeLog
%_libdir/libmemphis-%api.la
%_libdir/libmemphis-%api.so
%_includedir/libmemphis-%api/
%_libdir/pkgconfig/memphis-%api.pc
%_datadir/gtk-doc/html/libmemphis
%_datadir/gir-1.0/Memphis-%api.gir
