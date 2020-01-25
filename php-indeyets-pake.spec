%define		status		stable
%define		pearname	pake
Summary:	%{pearname} - PHP automation tool with capabilities similar to make
Name:		php-indeyets-pake
Version:	1.7.2
Release:	1
License:	BSD license
Group:		Development/Languages/PHP
Source0:	http://pear.indeyets.ru/get/%{pearname}-%{version}.tgz
# Source0-md5:	0678184f4493e45bc32105a2a2134d91
URL:		https://github.com/indeyets/pake/wiki
BuildRequires:	php-channel(pear.indeyets.ru)
BuildRequires:	php-packagexml2cl
BuildRequires:	php-pear-PEAR >= 1:1.4.1
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.654
Requires:	php(pcre)
Requires:	php-channel(pear.indeyets.ru)
Requires:	php-pear
Requires:	php-symfony-YAML
Suggests:	php(bz2)
Suggests:	php(mbstring)
Suggests:	php(pcntl)
Suggests:	php(phar)
Suggests:	php(posix)
Suggests:	php(svn)
Suggests:	php(yaml)
Suggests:	php(zlib)
Suggests:	php-pear-PEAR
Suggests:	php-phing
Suggests:	php-simpletest
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

# exclude optional dependencies
%define		_noautoreq_pear PEAR/.* PEAR2/Autoload.php phing/Phing.php simpletest/.*

%description
Pake is a command line utility for executing predefined tasks,
inspired by make. It is written in PHP and the tasks are also
described in PHP.

Pake supports tasks with prerequisites. Pake can be bundled with your
application as a single phar archive (or even as a single PHP file),
end users don’t need to install Pake on their systems.

Pake can be used for compiling projects from different pieces,
generating code, preprocessing templates and deploying projects.

In PEAR status of this package is: %{status}.

%prep
%pear_package_setup
mv docs/pake/* .

%build
packagexml2cl package.xml > ChangeLog

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{php_pear_dir}}
%pear_package_install
install -p ./%{_bindir}/* $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%post -p <lua>
%pear_package_print_optionalpackages

%files
%defattr(644,root,root,755)
%doc LICENSE ChangeLog install.log optional-packages.txt
%{php_pear_dir}/.registry/.channel.*/*.reg
%attr(755,root,root) %{_bindir}/pake
%{php_pear_dir}/pake.php
%{php_pear_dir}/pake
