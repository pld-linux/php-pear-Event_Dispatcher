%include	/usr/lib/rpm/macros.php
%define		_class		Event
%define		_subclass	Dispatcher
%define		_status		beta
%define		_pearname	%{_class}_%{_subclass}

Summary:	%{_pearname} - Dispatch notifications using PHP callbacks
#Summary(pl):	%{_pearname} -
Name:		php-pear-%{_pearname}
Version:	0.9.1
Release:	1
License:	BSD
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	975cab848349c5e190ff773b107796c0
URL:		http://pear.php.net/package/Event_Dispatcher/
BuildRequires:	rpm-php-pearprov >= 4.0.2-98
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

#%description -l pl
#...
#
#Ta klasa ma w PEAR status: %{_status}.

%prep
%setup -q -c

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}

install %{_pearname}-%{version}/*.php $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc %{_pearname}-%{version}/{tests,examples}
%{php_pear_dir}/%{_class}
