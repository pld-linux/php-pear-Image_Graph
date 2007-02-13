# ToDo:
# - update pl/en desription (sync with what's on pear's site)
#
%include	/usr/lib/rpm/macros.php
%define		_class		Image
%define		_subclass	Graph
%define		_status		alpha
%define		_pearname	%{_class}_%{_subclass}

Summary:	%{_pearname} - drawing graphs out of numerical data (traffic, money, ...)
Summary(pl.UTF-8):	%{_pearname} - rysowanie wykresów danych liczbowych (handel, pieniądze, ...)
Name:		php-pear-%{_pearname}
Version:	0.7.2
Release:	1
Epoch:		0
License:	PHP 2.02
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	4e3f338314fe0754970a896686875a5e
URL:		http://pear.php.net/package/Image_Graph/
BuildRequires:	php-pear-PEAR
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.300
Requires:	php-pear
Requires:	php-pear-Image_Canvas >= 0.3.0
Requires:	php-pear-PEAR-core >= 1:1.3.1
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

# exclude optional dependencies
%define		_noautoreq	'pear(Numbers/Roman.php)' 'pear(Numbers/Words.php)'

%description
Features:
- drawing graphs in various formats (line, bar, points marked by
  squares/rhombs/triangles/...)
- multiple graphs in one diagram
- up to 2 Y-axes
- flexible Y-value-output-customisation
- variable ticks for the Y-axes
- color-support
- ...

In PEAR status of this package is: %{_status}.

%description -l pl.UTF-8
Możliwości:
- rysowanie wykresów w różnych formatach (liniowym, słupkowym, punktów
  oznaczonych kwadratami/rombami/trójkątami...)
- wiele wykresów na jednym diagramie
- do dwóch osi Y
- elastyczne dostosowywanie wartości na osi Y
- zmienny krok dla osi Y
- obsługa koloru
- ...

Ta klasa ma w PEAR status: %{_status}.

%package tests
Summary:	Tests for PEAR::%{_pearname}
Summary(pl.UTF-8):	Testy dla PEAR::%{_pearname}
Group:		Development/Languages/PHP
Requires:	%{name} = %{epoch}:%{version}-%{release}
AutoReq:	no
AutoProv:	no

%description tests
Tests for PEAR::%{_pearname}.

%description tests -l pl.UTF-8
Testy dla PEAR::%{_pearname}.

%prep
%pear_package_setup

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}
%pear_package_install

%clean
rm -rf $RPM_BUILD_ROOT

%post
if [ -f %{_docdir}/%{name}-%{version}/optional-packages.txt ]; then
	cat %{_docdir}/%{name}-%{version}/optional-packages.txt
fi

%files
%defattr(644,root,root,755)
%doc install.log optional-packages.txt
%doc docs/%{_pearname}/docs
%{php_pear_dir}/.registry/*.reg
%{php_pear_dir}/%{_class}/*.php
%{php_pear_dir}/%{_class}/%{_subclass}

%files tests
%defattr(644,root,root,755)
%{php_pear_dir}/tests/*
