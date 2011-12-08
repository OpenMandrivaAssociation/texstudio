%define origname texstudio

Name:		texstudio
Summary:	Free cross-platform LaTeX editor
License:	GPLv2+
Version:	2.2
Release:	%mkrel 1
Source0:	http://prdownloads.sourceforge.net/texstudio/%{origname}-%{version}.tar.gz
URL:		http://texstudio.sourceforge.net/
Group:		Publishing
Buildroot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot 
BuildRequires:	qt4-devel
BuildRequires:	libpoppler-qt4-devel
Requires:	desktop-file-utils 
Obsoletes:  TexMakerX < 1.9.9-3
Obsoletes:	texmakerx < 2.2
Provides:   TeXstudio = %version-%release

%description
TeXstudio is a LaTeX IDE that gives you an environment where you can easily
create and manage LaTeX documents. It provides modern writing support, like interactive 
spell checking, code folding and syntax highlighting. Also it serves as a starting point 
from where you can easily run all necessary LaTeX tools.

%prep
%setup -q -n %{name}%{version}	

%build
%qmake_qt4 PREFIX=%{_prefix} texstudio.pro 
%make 

%install
%__rm -rf %{buildroot}
make install INSTALL_ROOT=%buildroot

%clean
%__rm -rf %{buildroot}

%files
%defattr(-,root,root) 
%{_datadir}/%{origname}/*
%{_datadir}/applications/texstudio.desktop
%{_bindir}/texstudio

