%define name	candido-themes
%define version 1.0
%define release %mkrel 5

%define themesdir %{_datadir}/themes

Summary:	  Themes for Candido
Name:    	  %{name}
Version: 	  %{version}
Release: 	  %{release}
Source0: 	  Candido-Calm.tar.bz2
Source1: 	  Candido-Candy.tar.bz2
Source2: 	  Candido-DarkOrange.tar.bz2
Source3: 	  Candido-Hybrid.tar.bz2
Source4: 	  Candido-NeoGraphite.tar.bz2
Source5: 	  Candido-Engine-Metacity.tar.bz2
Source6: 	  Candido-Engine-Xfwm4.tar.bz2
License: 	  GPL
Group: 		  Graphical desktop/GNOME
Url:   		  http://candido.berlios.de/
BuildRoot: 	  %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildArch: 	  noarch
Requires: 	  candido

%description
Various GTK2, Metacity, and XFWM4 themes for the Candido GTK2.x engine.

%prep

%build

%install
%__rm -rf %{buildroot}
%__mkdir -p %{buildroot}%{themesdir}
%__tar jfx %SOURCE0 -C %{buildroot}%{themesdir}
%__tar jfx %SOURCE1 -C %{buildroot}%{themesdir}
%__tar jfx %SOURCE2 -C %{buildroot}%{themesdir}
%__tar jfx %SOURCE3 -C %{buildroot}%{themesdir}
%__tar jfx %SOURCE4 -C %{buildroot}%{themesdir}
%__tar jfx %SOURCE5 -C %{buildroot}%{themesdir}
%__tar jfx %SOURCE6 -C %{buildroot}%{themesdir}

%clean
%__rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{themesdir}/*



%changelog
* Thu Dec 09 2010 Oden Eriksson <oeriksson@mandriva.com> 1.0-5mdv2011.0
+ Revision: 616937
- the mass rebuild of 2010.0 packages

* Wed Sep 02 2009 Thierry Vignaud <tv@mandriva.org> 1.0-4mdv2010.0
+ Revision: 424745
- rebuild

* Wed Jul 23 2008 Thierry Vignaud <tv@mandriva.org> 1.0-3mdv2009.0
+ Revision: 243432
- rebuild

* Wed Jan 09 2008 Lev Givon <lev@mandriva.org> 1.0-1mdv2008.1
+ Revision: 147369
- import candido-themes


* Wed Jan 09 2008 Lev Givon <lev@mandriva.org> 1.0-1mdv2008.0
- Package for Mandriva.
