#
# Conditional build:
%bcond_with	tests		# build without tests

%define	pkgname	cocoapods
Summary:	The Cocoa library package manager
Name:		ruby-%{pkgname}
Version:	0.39.0
Release:	0.1
License:	MIT
Group:		Development/Languages
Source0:	http://rubygems.org/downloads/%{pkgname}-%{version}.gem
# Source0-md5:	cb8e12483492ead3c580837c89fbf195
URL:		https://github.com/CocoaPods/CocoaPods
BuildRequires:	rpm-rubyprov
BuildRequires:	rpmbuild(macros) >= 1.656
BuildRequires:	sed >= 4.0
%if %{with tests}
BuildRequires:	ruby-bacon < 2
BuildRequires:	ruby-bacon >= 1.1
BuildRequires:	ruby-bundler < 2
BuildRequires:	ruby-bundler >= 1.3
BuildRequires:	ruby-rake < 11
BuildRequires:	ruby-rake >= 10.0
%endif
Requires:	ruby-activesupport >= 4.0.2
Requires:	ruby-claide < 0.10
Requires:	ruby-claide >= 0.9.1
Requires:	ruby-cocoapods-core = 0.39.0
Requires:	ruby-cocoapods-downloader < 0.10
Requires:	ruby-cocoapods-downloader >= 0.9.3
Requires:	ruby-cocoapods-plugins < 0.5
Requires:	ruby-cocoapods-plugins >= 0.4.2
Requires:	ruby-cocoapods-search < 0.2
Requires:	ruby-cocoapods-search >= 0.1.0
Requires:	ruby-cocoapods-stats < 0.7
Requires:	ruby-cocoapods-stats >= 0.6.2
Requires:	ruby-cocoapods-trunk < 0.7
Requires:	ruby-cocoapods-trunk >= 0.6.4
Requires:	ruby-cocoapods-try < 0.6
Requires:	ruby-cocoapods-try >= 0.5.1
Requires:	ruby-colored < 2
Requires:	ruby-colored >= 1.2
Requires:	ruby-escape < 0.1
Requires:	ruby-escape >= 0.0.4
Requires:	ruby-molinillo < 0.5
Requires:	ruby-molinillo >= 0.4.0
Requires:	ruby-nap < 2
Requires:	ruby-nap >= 1.0
Requires:	ruby-xcodeproj < 0.29
Requires:	ruby-xcodeproj >= 0.28.2
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
CocoaPods manages library dependencies for your Xcode project. You
specify the dependencies for your project in one easy text file.
CocoaPods resolves dependencies between libraries, fetches source code
for the dependencies, and creates and maintains an Xcode workspace to
build your project. Ultimately, the goal is to improve discoverability
of, and engagement in, third party open-source libraries, by creating
a more centralized ecosystem.

%prep
%setup -q -n %{pkgname}-%{version}
%{__sed} -i -e '1 s,#!.*ruby,#!%{__ruby},' bin/*

%build
# write .gemspec
%__gem_helper spec

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{ruby_vendorlibdir},%{ruby_specdir},%{_bindir}}
cp -a lib/* $RPM_BUILD_ROOT%{ruby_vendorlibdir}
cp -a bin/* $RPM_BUILD_ROOT%{_bindir}
cp -p %{pkgname}-%{version}.gemspec $RPM_BUILD_ROOT%{ruby_specdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/pod
%attr(755,root,root) %{_bindir}/sandbox-pod
%{ruby_vendorlibdir}/%{pkgname}.rb
%{ruby_vendorlibdir}/%{pkgname}
%{ruby_specdir}/%{pkgname}-%{version}.gemspec
