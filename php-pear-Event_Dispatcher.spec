%include	/usr/lib/rpm/macros.php
%define		_class		Event
%define		_subclass	Dispatcher
%define		_status		stable
%define		_pearname	%{_class}_%{_subclass}

Summary:	%{_pearname} - dispatch notifications using PHP callbacks
Summary(pl.UTF-8):	%{_pearname} - przekazywanie powiadomień za pośrednictwem callbacków PHP
Name:		php-pear-%{_pearname}
Version:	1.0.0
Release:	1
Epoch:		0
License:	BSD
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	0364b1bde5cbe770be9deb0a96cba6e2
URL:		http://pear.php.net/package/Event_Dispatcher/
BuildRequires:	php-pear-PEAR
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.300
Requires:	php-pear
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The Event_Dispatcher acts as a notification dispatch table. It is used
to notify other objects of interesting things. This information is
encapsulated in Event_Notification objects. Client objects register
themselves with the Event_Dispatcher as observers of specific
notifications posted by other objects. When an event occurs, an object
posts an appropriate notification to the Event_Dispatcher. The
Event_Dispatcher dispatches a message to each registered observer,
passing the notification as the sole argument.

In PEAR status of this package is: %{_status}.

%description -l pl.UTF-8
Event_Dispatcher działa jako tabela przekazywania powiadomień. Służy
do powiadamiania innych obiektów o interesujących rzeczach. Informacje
te są opakowywane w obiekty Event_Notification. Obiekty klienckie
rejestrują się w klasie Event_Dispatcher jako obserwatorzy konkretnych
powiadomień wysyłanych przez inne obiekty. Kiedy zachodzi zdarzenie,
obiekt wysyła odpowiednie powiadomienie do klasy Event_Dispatcher.
Event_Dispatcher przekazuje tę wiadomość do każdego zarejestrowanego
obserwatora, przekazując powiadomienie jako jedyny argument.

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

%files
%defattr(644,root,root,755)
%doc install.log
%doc docs/%{_pearname}/examples
%{php_pear_dir}/.registry/*.reg
%{php_pear_dir}/%{_class}

%files tests
%defattr(644,root,root,755)
%{php_pear_dir}/tests/*
