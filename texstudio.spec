Name:		texstudio
Summary:	Free cross-platform LaTeX editor
License:	GPLv2+
Version:	2.5.1
Release:	2
Source0:	http://downloads.sourceforge.net/project/texstudio/%{name}/TeXstudio%20%{version}/%{name}-%{version}.orig.tar.gz
URL:		http://texstudio.sourceforge.net/
Group:		Publishing
BuildRequires:	qt4-devel
BuildRequires:	pkgconfig(poppler-qt4)
Requires:	desktop-file-utils 

%description
TeXstudio is a LaTeX IDE that gives you an environment where you can easily
create and manage LaTeX documents. It provides modern writing support, like
interactive spell checking, code folding and syntax highlighting. Also it
serves as a starting point from where you can easily run all necessary LaTeX
tools.

%prep
%setup -q

%build
%qmake_qt4 PREFIX=%{_prefix} texstudio.pro 
%make 

%install
make install INSTALL_ROOT=%buildroot

%files
%{_datadir}/%{name}/*
%{_datadir}/applications/texstudio.desktop
%{_bindir}/texstudio



%changelog
* Thu Dec 08 2011 Lev Givon <lev@mandriva.org> 2.2-1mdv2012.0
+ Revision: 739086
- Update to 2.2.
- Rename to texstudio.

* Sun Jan 30 2011 Lev Givon <lev@mandriva.org> 2.0-1
+ Revision: 634301
- Update to 2.0.

* Sat Aug 07 2010 Nicolas Lécureuil <nlecureuil@mandriva.com> 1.9.9a-1mdv2011.0
+ Revision: 567368
- New version 1.9.9a
- Fix package name
- Clean buildroot before install ( removed in previous commit )

* Sat Aug 07 2010 Nicolas Lécureuil <nlecureuil@mandriva.com> 1.9.9-2mdv2011.0
+ Revision: 567357
- Fix release
- Fix use of translations
- Fix qt4-devel  Buildrequire

* Mon Jul 19 2010 Sandro Cazzaniga <kharec@mandriva.org> 1.9.9-1mdv2011.0
+ Revision: 554985
- import TexMakerX

