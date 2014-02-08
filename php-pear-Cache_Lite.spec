%define		_class		Cache
%define		_subclass	Lite
%define		upstream_name	%{_class}_%{_subclass}

Name:		php-pear-%{upstream_name}
Version:	1.7.11
Release:	5
Summary:	Fast and Safe little cache system
License:	PHP License
Group:		Development/PHP
URL:		http://pear.php.net/package/Cache_Lite/
Source0:	http://download.pear.php.net/package/%{upstream_name}-%{version}.tgz
Source1:	Hashed_Cache_Lite.php.bz2
Requires(post): php-pear
Requires(preun): php-pear
Requires:	php-pear
BuildArch:	noarch
BuildRequires:	php-pear

%description
This package is a little cache system optimized for file containers.
It is fast and safe (because it uses file locking and/or
anti-corruption tests).

%prep
%setup -q -c
mv package.xml %{upstream_name}-%{version}/%{upstream_name}.xml

%install
rm -rf %{buildroot}

cd %{upstream_name}-%{version}
pear install --nodeps --packagingroot %{buildroot} %{upstream_name}.xml
rm -rf %{buildroot}%{_datadir}/pear/.??*

rm -rf %{buildroot}%{_datadir}/pear/docs
rm -rf %{buildroot}%{_datadir}/pear/tests

install -d %{buildroot}%{_datadir}/pear/packages
install -m 644 %{upstream_name}.xml %{buildroot}%{_datadir}/pear/packages

%clean
rm -rf %{buildroot}



%files
%defattr(-,root,root)
%doc %{upstream_name}-%{version}/docs/*
%doc %{upstream_name}-%{version}/TODO
%{_datadir}/pear/%{_class}
%{_datadir}/pear/packages/%{upstream_name}.xml


%changelog
* Thu Jun 02 2011 Oden Eriksson <oeriksson@mandriva.com> 1.7.11-1mdv2011.0
+ Revision: 682489
- 1.7.11

* Mon May 30 2011 Oden Eriksson <oeriksson@mandriva.com> 1.7.10-1
+ Revision: 681795
- 1.7.10

* Wed May 04 2011 Oden Eriksson <oeriksson@mandriva.com> 1.7.9-2
+ Revision: 667485
- mass rebuild

* Mon Mar 07 2011 Oden Eriksson <oeriksson@mandriva.com> 1.7.9-1
+ Revision: 642442
- 1.7.9

* Fri Dec 03 2010 Oden Eriksson <oeriksson@mandriva.com> 1.7.8-3mdv2011.0
+ Revision: 607090
- rebuild

* Sun Dec 13 2009 Guillaume Rousse <guillomovitch@mandriva.org> 1.7.8-2mdv2010.1
+ Revision: 478288
- spec cleanup
- use pear installer
- don't ship tests, even in documentation
- own all directories
- use rpm filetriggers starting from mandriva 2010.1

* Fri Jul 10 2009 Guillaume Rousse <guillomovitch@mandriva.org> 1.7.8-1mdv2010.0
+ Revision: 394091
- update to new version 1.7.8

* Thu Mar 19 2009 Guillaume Rousse <guillomovitch@mandriva.org> 1.7.7-1mdv2009.1
+ Revision: 357905
- update to new version 1.7.7

* Sat Jan 24 2009 Funda Wang <fwang@mandriva.org> 1.7.5-1mdv2009.1
+ Revision: 333193
- update to new version 1.7.5

* Wed Dec 31 2008 Oden Eriksson <oeriksson@mandriva.com> 1.7.4-2mdv2009.1
+ Revision: 321799
- rebuild

* Sat Aug 16 2008 Oden Eriksson <oeriksson@mandriva.com> 1.7.4-1mdv2009.0
+ Revision: 272581
- 1.7.4

* Wed Jun 18 2008 Thierry Vignaud <tv@mandriva.org> 1.7.2-4mdv2009.0
+ Revision: 224687
- rebuild

* Tue Mar 04 2008 Oden Eriksson <oeriksson@mandriva.com> 1.7.2-3mdv2008.1
+ Revision: 178500
- rebuild

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Thu Aug 16 2007 Thierry Vignaud <tv@mandriva.org> 1.7.2-2mdv2008.0
+ Revision: 64201
- rebuild

* Fri Apr 20 2007 Oden Eriksson <oeriksson@mandriva.com> 1.7.2-1mdv2008.0
+ Revision: 15533
- 1.7.2


* Sat Nov 11 2006 Oden Eriksson <oeriksson@mandriva.com> 1.7.1-1mdv2007.0
+ Revision: 81072
- Import php-pear-Cache_Lite

* Sat May 20 2006 Oden Eriksson <oeriksson@mandriva.com> 1.7.1-1mdk
- 1.7.1

* Sat Apr 08 2006 Oden Eriksson <oeriksson@mandriva.com> 1.7.0-1mdk
- 1.7.0

* Fri Feb 10 2006 Oden Eriksson <oeriksson@mandriva.com> 1.6.0-1mdk
- 1.6.0
- added the Hashed_Cache_Lite.php class from phpgacl-3.3.6

* Fri Aug 26 2005 Oden Eriksson <oeriksson@mandriva.com> 1.5.2-4mdk
- rebuilt to fix auto deps

* Wed Aug 10 2005 Oden Eriksson <oeriksson@mandriva.com> 1.5.2-3mdk
- rebuilt to use new pear auto deps/reqs from pld

* Sun Jul 31 2005 Oden Eriksson <oeriksson@mandriva.com> 1.5.2-2mdk
- fix deps

* Thu Jul 21 2005 Oden Eriksson <oeriksson@mandriva.com> 1.5.2-1mdk
- 1.5.2

* Thu Jul 21 2005 Oden Eriksson <oeriksson@mandriva.com> 1.4.1-3mdk
- reworked the %%post and %%preun stuff, like in conectiva
- fix deps

* Wed Jul 20 2005 Oden Eriksson <oeriksson@mandriva.com> 1.4.1-2mdk
- fix deps

* Tue Jul 19 2005 Oden Eriksson <oeriksson@mandriva.com> 1.4.1-1mdk
- initial Mandriva package (PLD import)

