# TODO:
# - update pl/en desription (sync with what's on pear's site)

%define		_status		alpha
%define		_pearname	Image_Graph
Summary:	%{_pearname} - drawing graphs out of numerical data (traffic, money, ...)
Summary(pl.UTF-8):	%{_pearname} - rysowanie wykresów danych liczbowych (handel, pieniądze, ...)
Name:		php-pear-%{_pearname}
Version:	0.8.0
Release:	1
License:	PHP 2.02
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	8755a8a86b4fd0fe8aa0bc13ed98f598
URL:		http://pear.php.net/package/Image_Graph/
BuildRequires:	php-pear-PEAR >= 1:1.4.0-0.b1
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.571
Requires:	php-pear
Requires:	php-pear-Image_Canvas >= 0.3.0
Requires:	php-pear-PEAR-core >= 1:1.3.1
Suggests:	php-pear-Numbers_Roman
Suggests:	php-pear-Numbers_Words
Obsoletes:	php-pear-Image_Graph-tests
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

%prep
%pear_package_setup

# packagers junk
rm -f .%{php_pear_dir}/data/Image_Graph/.project
rm -f .%{php_pear_dir}/data/Image_Graph/gendocHTML.sh
rm -f .%{php_pear_dir}/data/Image_Graph/gendocPeardoc2.sh

mv docs/%{_pearname}/docs/examples .

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}
%pear_package_install

install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
cp -a examples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%post -p <lua>
%pear_package_print_optionalpackages

%files
%defattr(644,root,root,755)
%doc install.log optional-packages.txt
%doc docs/%{_pearname}/docs/*
%{php_pear_dir}/.registry/*.reg
%{php_pear_dir}/Image/Graph.php
%{php_pear_dir}/Image/Graph

%{_examplesdir}/%{name}-%{version}
