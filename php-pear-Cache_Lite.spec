%define		_class		Cache
%define		_subclass	Lite
%define		upstream_name	%{_class}_%{_subclass}

Summary:	Fast and Safe little cache system
Name:		php-pear-%{upstream_name}
Version:	1.7.11
Release:	6
License:	PHP License
Group:		Development/PHP
Url:		http://pear.php.net/package/Cache_Lite/
Source0:	http://download.pear.php.net/package/%{upstream_name}-%{version}.tgz
Source1:	Hashed_Cache_Lite.php.bz2
BuildArch:	noarch
BuildRequires:	php-pear
Requires(post,preun):	php-pear
Requires:	php-pear

%description
This package is a little cache system optimized for file containers.
It is fast and safe (because it uses file locking and/or
anti-corruption tests).

%prep
%setup -q -c
mv package.xml %{upstream_name}-%{version}/%{upstream_name}.xml

%install
cd %{upstream_name}-%{version}
pear install --nodeps --packagingroot %{buildroot} %{upstream_name}.xml
rm -rf %{buildroot}%{_datadir}/pear/.??*

rm -rf %{buildroot}%{_datadir}/pear/docs
rm -rf %{buildroot}%{_datadir}/pear/tests

install -d %{buildroot}%{_datadir}/pear/packages
install -m 644 %{upstream_name}.xml %{buildroot}%{_datadir}/pear/packages

%files
%doc %{upstream_name}-%{version}/docs/*
%doc %{upstream_name}-%{version}/TODO
%{_datadir}/pear/%{_class}
%{_datadir}/pear/packages/%{upstream_name}.xml

