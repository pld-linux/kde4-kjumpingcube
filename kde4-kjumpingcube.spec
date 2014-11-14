%define		_state		stable
%define		orgname		kjumpingcube
%define		qtver		4.8.0

Summary:	A little tactical game for KDE
Summary(pl.UTF-8):	Prosta gra taktyczna dla KDE
Summary(pt_BR.UTF-8):	Jogo de estratégia para 2 contendores
Name:		kde4-%{orgname}
Version:	4.14.3
Release:	1
License:	GPL
Group:		X11/Applications/Games
Source0:	http://download.kde.org/%{_state}/%{version}/src/%{orgname}-%{version}.tar.xz
# Source0-md5:	70cb53a01ff1f215130898560c049806
BuildRequires:	automoc4 >= 0.9.88
BuildRequires:	cmake >= 2.8.0
BuildRequires:	kde4-kdelibs-devel >= %{version}
BuildRequires:	kde4-libkdegames-devel >= %{version}
BuildRequires:	qt4-build >= %{qtver}
BuildRequires:	qt4-qmake >= %{qtver}
BuildRequires:	rpmbuild(macros) >= 1.600
Obsoletes:	kde4-kdegames-%{orgname}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
KJumpingCube is a simple tactical game. You can play it against the
computer or against the friend. The playing field consists of squares
that contains points. By clicking on the squares you can increase the
points, and if the points reach a maximum the points will jump to the
squares neighbours and take them over. Winer is the one, who owns all
squares.

%description -l pl.UTF-8
KJumpingCube to prosta gra taktyczna. Można w nią grać przeciwko
komputerowi lub przeciwko koledze. Plansza do gry zawiera pola, które
zawierają punkty. Przez klikanie na pola zwiększa się liczbę punktów
na nich. Gdy liczba punktów na określonym polu osiągnie maksymalną
wartość, punkty przeskakują na sąsiednie pola przejmując je tym samym
na własność. Zwycięzca jest jeden - to ten, kto przejmie wszystkie
pola na własność.

%description -l pt_BR.UTF-8
Jogo de estratégia para 2 contendores.

%prep
%setup -q -n %{orgname}-%{version}

%build
install -d build
cd build
%cmake \
	../

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT \
	kde_htmldir=%{_kdedocdir}

install -d $RPM_BUILD_ROOT/var/games
# remove locolor icons
rm -rf $RPM_BUILD_ROOT%{_iconsdir}/locolor

%find_lang %{orgname}	--with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{orgname}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kjumpingcube
%{_desktopdir}/kde4/kjumpingcube.desktop
%{_datadir}/config.kcfg/kjumpingcube.kcfg
%{_datadir}/apps/kjumpingcube
%{_iconsdir}/*/*/apps/kjumpingcube.png
