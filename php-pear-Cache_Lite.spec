%define		_class		Cache
%define		_subclass	Lite
%define		upstream_name	%{_class}_%{_subclass}

%define _requires_exceptions pear(Cache/Lite/Lite.php)

Name:		php-pear-%{upstream_name}
Version:	1.7.9
Release:	%mkrel 2
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
BuildRoot:	%{_tmppath}/%{name}-%{version}

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

%post
%if %mdkversion < 201000
pear install --nodeps --soft --force --register-only \
    %{_datadir}/pear/packages/%{upstream_name}.xml >/dev/null || :
%endif

%preun
%if %mdkversion < 201000
if [ "$1" -eq "0" ]; then
    pear uninstall --nodeps --ignore-errors --register-only \
        %{pear_name} >/dev/null || :
fi
%endif

%files
%defattr(-,root,root)
%doc %{upstream_name}-%{version}/docs/*
%doc %{upstream_name}-%{version}/TODO
%{_datadir}/pear/%{_class}
%{_datadir}/pear/packages/%{upstream_name}.xml
