Name:		texstudio
Summary:	Free cross-platform LaTeX editor
License:	GPLv2+
Version:	4.5.2
Release:	1
Source0:	https://github.com/texstudio-org/texstudio/archive/refs/tags/%{version}.tar.gz
URL:		http://texstudio.sourceforge.net/
Patch0:		texstudio-4.2.0-fix-system-quazip.patch
Group:		Publishing
BuildRequires:	qt5-devel
BuildRequires:	pkgconfig(poppler-cpp)
BuildRequires:	pkgconfig(poppler-qt5)
BuildRequires:	pkgconfig(quazip1-qt5)
BuildRequires:	pkgconfig(Qt5Svg)
BuildRequires:	pkgconfig(Qt5Script)
BuildRequires:	pkgconfig(Qt5UiTools)
Requires:	desktop-file-utils 

%description
TeXstudio is a LaTeX IDE that gives you an environment where you can easily
create and manage LaTeX documents. It provides modern writing support, like
interactive spell checking, code folding and syntax highlighting. Also it
serves as a starting point from where you can easily run all necessary LaTeX
tools.

%prep
%autosetup -p1

%build
%qmake_qt5 PREFIX=%{_prefix} USE_SYSTEM_QUAZIP=1 texstudio.pro 
%make_build

%install
make install INSTALL_ROOT=%buildroot STRIP=echo

%files
%{_datadir}/%{name}/*
%{_datadir}/metainfo/texstudio.metainfo.xml
%{_datadir}/applications/texstudio.desktop
%{_datadir}/icons/hicolor/scalable/apps/texstudio.svg
%{_bindir}/texstudio
