%include	/usr/lib/rpm/macros.php
%define         _class          Image
%define         _subclass       Graph
%define		_status		alpha
%define		_pearname	%{_class}_%{_subclass}

Summary:	%{_pearname} - drawing graphs out of numerical data (traffic, money, ...)
Summary(pl):	%{_pearname} - rysowanie wykresów danych liczbowych (handel, pieni±dze, ...)
Name:		php-pear-%{_pearname}
Version:	0.1.1
Release:	1
License:	PHP 2.02
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	77d6c7ba11be8d315657e06146908814
URL:		http://pear.php.net/package/Image_Graph/
BuildRequires:	rpm-php-pearprov >= 4.0.2-98
Requires:	php-pear
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

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

This class has in PEAR status: %{_status}.

%description -l pl
Mo¿liwo¶ci:
- rysowanie wykresów w ró¿nych formatach (liniowym, s³upkowym, punktów
  oznaczonych kwadratami/rombami/trójk±tami...)
- wiele wykresów na jednym diagramie
- do dwóch osi Y
- elastyczne dostosowywanie warto¶ci na osi Y
- zmienny krok dla osi Y
- obsluga koloru
- ...

Ta klasa ma w PEAR status: %{_status}.

%prep
%setup -q -c

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/%{_subclass}

install %{_pearname}-%{version}/*.php              $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}
install %{_pearname}-%{version}/%{_subclass}/*.php $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/%{_subclass}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc %{_pearname}-%{version}/docs
%dir %{php_pear_dir}/%{_class}/%{_subclass}
%{php_pear_dir}/%{_class}/*.php
%{php_pear_dir}/%{_class}/%{_subclass}/*.php
