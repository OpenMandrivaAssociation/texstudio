Name:		texstudio
Summary:	Free cross-platform LaTeX editor
License:	GPLv2+
Version:	4.9.2
Release:	1
Source0:	https://github.com/texstudio-org/texstudio/archive/refs/tags/%{version}.tar.gz
URL:		https://texstudio.sourceforge.net/
Patch0:		texstudio-4.2.0-fix-system-quazip.patch
Group:		Publishing
BuildSystem:	cmake
BuildRequires:	pkgconfig(poppler-cpp)
BuildRequires:	pkgconfig(poppler-qt6)
BuildRequires:	pkgconfig(quazip1-qt6)
BuildRequires:	pkgconfig(Qt6Core)
BuildRequires:	pkgconfig(Qt6Core5Compat)
BuildRequires:  pkgconfig(Qt6Network)
BuildRequires:  pkgconfig(Qt6Xml)
BuildRequires:  pkgconfig(Qt6Concurrent)
BuildRequires:	pkgconfig(Qt6Widgets)
BuildRequires:	pkgconfig(Qt6Svg)
BuildRequires:	pkgconfig(Qt6UiPlugin)
BuildRequires:	pkgconfig(Qt6UiTools)
BuildRequires:  pkgconfig(Qt6PrintSupport)
BuildRequires:  pkgconfig(Qt6Qml)
BuildRequires:  pkgconfig(Qt6Svg)
BuildRequires:  pkgconfig(Qt6Linguist)
Requires:	desktop-file-utils 

%description
TeXstudio is a LaTeX IDE that gives you an environment where you can easily
create and manage LaTeX documents. It provides modern writing support, like
interactive spell checking, code folding and syntax highlighting. Also it
serves as a starting point from where you can easily run all necessary LaTeX
tools.

%prep -a
rm -rf {hunspell,qtsingleapplication,quazip}
# force qt6
sed -i 's/Qt5//' CMakeLists.txt
 
%files
%{_datadir}/%{name}/*
%{_datadir}/metainfo/texstudio.metainfo.xml
%{_datadir}/applications/texstudio.desktop
%{_datadir}/icons/hicolor/scalable/apps/texstudio.svg
%{_bindir}/texstudio
%doc %{_docdir}/texstudio
