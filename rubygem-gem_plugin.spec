%define oname gem_plugin

Name:       rubygem-%{oname}
Version:    0.2.3
Release:    2
Summary:    A plugin system based on rubygems that uses dependencies only
Group:      Development/Ruby
License:    GPLv2+
URL:        http://rubydoc.info/gems/%{oname}/%{version}/frames
Source0:    http://rubygems.org/gems/%{oname}-%{version}.gem
BuildRoot:  %{_tmppath}/%{name}-%{version}-%{release}-root
Requires:   rubygems
BuildRequires: rubygems
BuildArch:  noarch
Provides:   rubygem(%{oname}) = %{version}

%description
A plugin system based on rubygems that uses dependencies only


%prep

%build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{ruby_gemdir}
gem install --local --install-dir %{buildroot}%{ruby_gemdir} \
            --force --rdoc %{SOURCE0}
mkdir -p %{buildroot}/%{_bindir}
mv %{buildroot}%{ruby_gemdir}/bin/* %{buildroot}/%{_bindir}
rmdir %{buildroot}%{ruby_gemdir}/bin
find %{buildroot}%{ruby_gemdir}/gems/%{oname}-%{version}/bin -type f | xargs chmod a+x
sed -i -e '1i#!/usr/bin/env ruby' %{buildroot}%{ruby_gemdir}/gems/%{oname}-%{version}/bin/gpgen

%clean
rm -rf %{buildroot}

%files
%defattr(-, root, root, -)
%{_bindir}/gpgen
%dir %{ruby_gemdir}/gems/%{oname}-%{version}/
%{ruby_gemdir}/gems/%{oname}-%{version}/bin/
%{ruby_gemdir}/gems/%{oname}-%{version}/lib/
%{ruby_gemdir}/gems/%{oname}-%{version}/test/
%{ruby_gemdir}/gems/%{oname}-%{version}/setup.rb
%{ruby_gemdir}/gems/%{oname}-%{version}/resources/lib/
%{ruby_gemdir}/gems/%{oname}-%{version}/resources/resources/
%doc %{ruby_gemdir}/doc/%{oname}-%{version}
%{ruby_gemdir}/cache/%{oname}-%{version}.gem
%{ruby_gemdir}/specifications/%{oname}-%{version}.gemspec
%doc %{ruby_gemdir}/gems/%{oname}-%{version}/CHANGELOG
%doc %{ruby_gemdir}/gems/%{oname}-%{version}/COPYING
%doc %{ruby_gemdir}/gems/%{oname}-%{version}/LICENSE
%doc %{ruby_gemdir}/gems/%{oname}-%{version}/Manifest
%doc %{ruby_gemdir}/gems/%{oname}-%{version}/README
%doc %{ruby_gemdir}/gems/%{oname}-%{version}/resources/COPYING
%doc %{ruby_gemdir}/gems/%{oname}-%{version}/resources/LICENSE
%doc %{ruby_gemdir}/gems/%{oname}-%{version}/resources/README
%doc %{ruby_gemdir}/gems/%{oname}-%{version}/resources/Rakefile
%doc %{ruby_gemdir}/gems/%{oname}-%{version}/%{oname}.gemspec


%changelog
* Mon Dec 20 2010 Rémy Clouard <shikamaru@mandriva.org> 0.2.3-1mdv2011.0
+ Revision: 623491
- import rubygem-gem_plugin

