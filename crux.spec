
%define		_name		crux

Summary:	Crux theme for GTK+2 and GNOME2
Summary(pl):	Motyw crux dla GTK+2 i ¶rodowiska GNOME2
Name:		crux-theme
Version:	1.9.5
Release:	2
License:	GPL
Group:		Themes
Source0:	http://ftp.gnome.org/pub/gnome/sources/%{_name}/1.9/%{_name}-%{version}.tar.bz2
# Source0-md5:	661285363026dcc79354c8804eb2cb1d
URL:		http://www.gnome.org/
BuildRequires:	autoconf
BuildRequires:	automake
Requires:	%{_name}-icons = %{version}
Requires:	%{_name}-engine = %{version}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The Crux theme (both a GTK2 engine and an icon theme).

%description -l pl
Motyw crux (motywy dla GTK2 i zestaw ikon).

%package -n %{_name}-engine
Summary:	Crux theme engine
Summary(pl):	Motyw Crux
Group:		Themes

%description -n %{_name}-engine
Crux theme engine.

%description -n %{_name}-engine -l pl
Motyw Crux.

%package -n %{_name}-icons
Summary:	Icons for Crux theme
Summary(pl):	Ikony dla motywu Crux
Group:		Themes

%description -n %{_name}-icons
Icons for Crux theme.

%description -n %{_name}-icons -l pl
Ikony dla motywu Crux.

%prep
%setup -q -n %{_name}-%{version}

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
%{_datadir}/themes/Crux

%files -n %{_name}-engine
%defattr(644,root,root,755)
%{_libdir}/gtk-2.0/*/engines/libcrux-engine.*
%{_datadir}/eazel-engine

%files -n %{_name}-icons
%defattr(644,root,root,755)
%{_datadir}/icons/Crux
