# ToDo:
# - update pl/en desription (sync with what's on pear's site)
#
%include	/usr/lib/rpm/macros.php
%define		_class		Image
%define		_subclass	Graph
%define		_status		alpha
%define		_pearname	%{_class}_%{_subclass}

Summary:	%{_pearname} - drawing graphs out of numerical data (traffic, money, ...)
Summary(pl):	%{_pearname} - rysowanie wykresów danych liczbowych (handel, pieni±dze, ...)
Name:		php-pear-%{_pearname}
Version:	0.6.0
Release:	1
License:	PHP 2.02
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	2f144455886000e5b230629e4ad71845
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

In PEAR status of this package is: %{_status}.

%description -l pl
Mo¿liwo¶ci:
- rysowanie wykresów w ró¿nych formatach (liniowym, s³upkowym, punktów
  oznaczonych kwadratami/rombami/trójk±tami...)
- wiele wykresów na jednym diagramie
- do dwóch osi Y
- elastyczne dostosowywanie warto¶ci na osi Y
- zmienny krok dla osi Y
- obs³uga koloru
- ...

Ta klasa ma w PEAR status: %{_status}.

%prep
%setup -q -c

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/%{_subclass}/{Axis/Marker,DataPreprocessor,DataSelector,Dataset,Figure,Fill,Grid,Images/{Icons,Maps},Layout,Line,Marker/Pointing,Plot/Smoothed,Plotarea}

install %{_pearname}-%{version}/*.php				$RPM_BUILD_ROOT%{php_pear_dir}/%{_class}
install %{_pearname}-%{version}/%{_subclass}/*.php				$RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/%{_subclass}
install %{_pearname}-%{version}/%{_subclass}/Axis/*.php		$RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/%{_subclass}/Axis
install %{_pearname}-%{version}/%{_subclass}/Axis/Marker/*.php	$RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/%{_subclass}/Axis/Marker
install %{_pearname}-%{version}/%{_subclass}/DataPreprocessor/*.php	$RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/%{_subclass}/DataPreprocessor
install %{_pearname}-%{version}/%{_subclass}/DataSelector/*.php	$RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/%{_subclass}/DataSelector
install %{_pearname}-%{version}/%{_subclass}/Dataset/*.php	$RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/%{_subclass}/Dataset
install %{_pearname}-%{version}/%{_subclass}/Figure/*.php	$RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/%{_subclass}/Figure
install %{_pearname}-%{version}/%{_subclass}/Fill/*.php		$RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/%{_subclass}/Fill
install %{_pearname}-%{version}/%{_subclass}/Grid/*.php		$RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/%{_subclass}/Grid
install %{_pearname}-%{version}/%{_subclass}/Images/Icons/*	$RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/%{_subclass}/Images/Icons
install %{_pearname}-%{version}/%{_subclass}/Images/Maps/*	$RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/%{_subclass}/Images/Maps
install %{_pearname}-%{version}/%{_subclass}/Layout/*.php	$RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/%{_subclass}/Layout
install %{_pearname}-%{version}/%{_subclass}/Line/*.php		$RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/%{_subclass}/Line
install %{_pearname}-%{version}/%{_subclass}/Marker/*.php	$RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/%{_subclass}/Marker
install %{_pearname}-%{version}/%{_subclass}/Marker/Pointing/*.php	$RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/%{_subclass}/Marker/Pointing
install %{_pearname}-%{version}/%{_subclass}/Plot/*.php		$RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/%{_subclass}/Plot
install %{_pearname}-%{version}/%{_subclass}/Plot/Smoothed/*.php	$RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/%{_subclass}/Plot/Smoothed
install %{_pearname}-%{version}/%{_subclass}/Plotarea/*.php	$RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/%{_subclass}/Plotarea

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc %{_pearname}-%{version}/docs
%{php_pear_dir}/%{_class}/*.php
%{php_pear_dir}/%{_class}/%{_subclass}
