Summary:	Crux theme for GTK+2 and GNOME2
Summary(pl.UTF-8):	Motyw Crux dla GTK+2 i środowiska GNOME2
Name:		crux
Version:	1.9.5
Release:	2
License:	GPL
Group:		Themes
Source0:	http://ftp.gnome.org/pub/gnome/sources/crux/1.9/%{name}-%{version}.tar.bz2
# Source0-md5:	661285363026dcc79354c8804eb2cb1d
URL:		http://www.gnome.org/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The Crux theme (both a GTK2 engine and an icon theme).

%description -l pl.UTF-8
Motyw Crux (motywy dla GTK2 i zestaw ikon).

%package theme
Summary:	Crux theme for GTK+2 and GNOME2
Summary(pl.UTF-8):	Motyw Crux dla GTK+2 i środowiska GNOME2
Group:		Themes
Requires:	%{name}-icons = %{version}-%{release}
Requires:	%{name}-engine = %{version}-%{release}

%description theme
The Crux theme (both a GTK2 engine and an icon theme).

%description theme -l pl.UTF-8
Motyw Crux (motywy dla GTK2 i zestaw ikon).

%package engine
Summary:	Crux theme engine
Summary(pl.UTF-8):	Silnik motywu Crux
Group:		Themes

%description engine
Crux theme engine.

%description engine -l pl.UTF-8
Silnik motywu Crux.

%package icons
Summary:	Icons for Crux theme
Summary(pl.UTF-8):	Ikony dla motywu Crux
Group:		Themes

%description icons
Icons for Crux theme.

%description icons -l pl.UTF-8
Ikony dla motywu Crux.

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

%files theme
%defattr(644,root,root,755)
%{_datadir}/themes/Crux

%files engine
%defattr(644,root,root,755)
%{_libdir}/gtk-2.0/*/engines/libcrux-engine.*
%{_datadir}/eazel-engine

%files icons
%defattr(644,root,root,755)
%{_datadir}/icons/Crux
