#
# Licensed to the Apache Software Foundation (ASF) under one or more
# contributor license agreements.  See the NOTICE file distributed with
# this work for additional information regarding copyright ownership.
# The ASF licenses this file to You under the Apache License, Version 2.0
# (the "License"); you may not use this file except in compliance with
# the License.  You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

%global         package_version 0.13.0-0
%global         package_name redhat-support-tool
%global         python_sitelib /usr/lib/python3.6/site-packages

Name:           %{package_name}
Version:        0.13.0
Release:        0%{?release_suffix}%{?dist}
Summary:        Tool for console access to Red Hat subscriber services
Vendor:         Red Hat, Inc.
Group:          Development/Libraries
License:        ASL 2.0
URL:            https://api.access.redhat.com
Source0:        http://people.redhat.com/kroberts/projects/redhat-support-tool/%{package_name}-%{package_version}.tar.gz

BuildRequires: python3-devel
BuildRequires: python3-setuptools
BuildArch: noarch
%{!?dist:BuildRequires: buildsys-macros}

Requires: python3
Requires: python3-lxml
Requires: python3-magic
Requires: python3-dateutil
Requires: python3-requests
Requires: python3-pexpect
Requires: nmap-ncat
Requires: redhat-support-lib-python >= 0.13.0-0

BuildRoot: %{_topdir}/BUILDROOT/%{name}-%{version}-%{release}.%{_arch}

%description
This package contains the Red Hat Support Tool.  The Red Hat Support Tool
provides console based access to Red Hat's subscriber services.  These
services include, but are not limited to, console based access to
knowledge-base solutions, case management, automated diagnostic
services, etc.

%prep
%setup -q -n %{package_name}-%{package_version}

%build
%configure \
        --disable-python-syntax-check

make %{?_smp_mflags}

# For sample vendor plugin
mkdir -p samples/vendors/
mv src/redhat_support_tool/vendors/ACMECorp samples/vendors/

%install
rm -rf "%{buildroot}"
make %{?_smp_mflags} install DESTDIR="%{buildroot}"

%files
%doc AUTHORS README README.plugins samples/
%{python_sitelib}/redhat_support_tool/
%{_bindir}/redhat-support-tool

%changelog
* Wed Dec 08 2021 Pranita Ghole<pghole@redhat.com> - 0.13.0-0
- Resolves: rhbz#2028556 - RHST should use new Red Hat Secure FTP instead of dropbox for attachments
- Resolves: rhbz#2028553 - Add support for handling JSON response from API's
- Resolves: rhbz#2028540 - Add support to upload to and download from S3

* Tue Nov 10 2020 Pranita Ghole<pghole@redhat.com> - 0.11.3-2
- Resolves: rhbz#1882771 - redhat-support-tool: UnboundLocalError: local variable 'timer' referenced before assignment
- Resolves: rhbz#1882772 - [RFE] Add functionality to generate and send sosreport after selecting the case.
- Resolves: rhbz#1882773 - [RFE] Generate and upload sosreport to case from cli

* Tue Feb 18 2020 Pranita Ghole<pghole@redhat.com> - 0.11.2-2
- Resolves: rhbz#1685296 - redhat-support-tool env var http_proxy does not work with user and password
- Resolves: rhbz#1685295 - [RFE][RHEL8] Include Reason in cases of failed proxy
- Resolves: rhbz#1684321 - redhat-support-tool config debug <level>` fails with "ERROR: debug is not a valid configuration file option.

* Thu Mar 28 2019 AP Rajshekhar<randalap@redhat.com> - 0.10.1-2
- Resolves: rhbz#1680690 - redhat-support-tool changes blocked until gating tests are added

* Fri Feb 08 2019 Pranita Ghole<pghole@redhat.com> - 0.10.1-1
- Resolves: rhbz#1670001 - redhat-support-tool -o option does not work (soscleaner)
- Resolves: rhbz#1670369 - redhat-support-lib-python: Traceback on make_report from utils.reporthelper
- Resolves: rhbz#1670044 - redhat-support-tool proxy does not work on rhel-8

* Mon Jan 21 2019 Vikas Rathee <vrathee@redhat.com> - 0.10.1-0
- Resolves: rhbz#1628538 - Fixing python 3 issues and using latest redhat-support-lib-python

* Wed Nov 21 2018 Vikas Rathee <vrathee@redhat.com> - 0.10.0-0
- Resolves: rhbz#1628538 - Changes for rhel-8

* Thu Nov 2 2017 Vikas Rathee <vrathee@redhat.com> - 0.9.10-1
- Resolves: rhbz#1342627 - List cases by group.
- Resolves: rhbz#1379619 - Inform when http_proxy environment variable is used.

* Wed May 31 2017 Vikas Rathee <vrathee@redhat.com> - 0.9.9-3
- Resolves: rhbz#1380109 - Correcting spacing in non-interactive mode search results.

* Thu May 25 2017 Vikas Rathee <vrathee@redhat.com> - 0.9.9-2
- Resolves: rhbz#1380109 - Include last modified date for solutions in non-interactive mode search

* Thu Apr 27 2017 Vikas Rathee <vrathee@redhat.com> - 0.9.9-1
- Resolves: rhbz#1380109 - Include creation date and last modified date in Solution title details.
- Resolves: rhbz#1342628 - When opening a new case, offer a default product.
- Resolves: rhbz#1342632 - When opening a new case, offer to use the default case group of that user.

* Tue Jul 5 2016 Mark Huth <mhuth@redhat.com> - 0.9.8-6
- Resolves: rhbz#1104344 - add soscleaner
- Resolves: rhbz#1273976 - caches bad password
- Resolves: rhbz#1284306 - improve ? help
- Resolves: rhbz#1284308 - show attachment sizes
- Resolves: rhbz#1284309 - show attachment full path
- Resolves: rhbz#1284314 - differentiate diagnose and analyze
- Resolves: rhbz#1290909 - change case internal status
- Resolves: rhbz#1351141 - reverse severity list

* Wed Mar 4 2015 Mark Huth <mhuth@redhat.com> - 0.9.7-4
- Resolves: rhbz#1196297 - typos in opencase
- Resolves: rhbz#1196316 - change menus when closing a case
- Fallback to ownerSSOName if associateSSOName filter gets 404 error in listcases
- Other small fixes

* Wed Jan 7 2015 Mark Huth <mhuth@redhat.com> - 0.9.7-3
- Resolves: rhbz#1168414 - rhel7 vmcore offset
- Resolves: rhbz#1174461 - skip already downloaded attachments
- Resolves: rhbz#1176473 - fix addattachment via FTP and proxy
- Make debug_repos configurable via config option

* Thu Nov 13 2014 Mark Huth <mhuth@redhat.com> - 0.9.7-2
- bz1161141 - search plugin output gives URLs to the XML page, not html
- bz1122161 - rfe for comment numbers and public/private markers in Case Discussion in getcase
- bz1122164 - rfe for ability to add private comments and attachments to a case

* Mon Oct 20 2014 Keith Robertson <kroberts@redhat.com> - 0.9.7-1
- Allow the CLI to return more than 50 results
- TypeError: Incorrect padding with a specific password and not working further.
- diagnose filename output gives URLs to the XML file, not html, and XML displays author sso name
- getcase subcommand of redhat-support-tool doesn't show the group name

* Fri Sep 5 2014 Keith Robertson <kroberts@redhat.com> - 0.9.6-3
- Fix btextract in non-interactive mode

* Thu Jun 19 2014 Keith Robertson <kroberts@redhat.com> - 0.9.6-2
- Display download progess for attachments
- Fix list attachments duplicates

* Wed Feb 26 2014 Keith Robertson <kroberts@redhat.com> - 0.9.6-0
- Various fixes

* Wed Aug 14 2013 Keith Robertson <kroberts@redhat.com> - 0.9.5-8
- Resolves: rhbz#987168

* Tue Jul 23 2013 Keith Robertson <kroberts@redhat.com> - 0.9.5-6
- Various RHEL 5 issues

* Mon Jul 22 2013 Keith Robertson <kroberts@redhat.com> - 0.9.5-4
- Resolves: rhbz#983909
- Resolves: rhbz#983896
- Resolves: rhbz#983903
- Also various issues with btextract

* Tue Jun 11 2013 Keith Robertson <kroberts@redhat.com> - 0.9.5-3
- Resolves: bz880766

* Tue Jun 11 2013 Keith Robertson <kroberts@redhat.com> - 0.9.5-2
- Various updates including;
  - Filtering and pagination of listcases
  - casegroup command
  - opencase is in the analyze and diagnose commands
  
* Thu May 23 2013 Nigel Jones <nigjones@redhat.com> - 0.9.4-1
- Diagnostics:
  - Opening a case will now trigger the case recommendations engine
    prior to opening the case.
  - Extracted backtraces from kernel vmcores can be passed to
    Ask Shadowman at the users request
- Case Handling:
  - modifycase can be triggered on a selected case
  - Per above, opencase/diagnostics support
- Plugins:
  - Ability for Vendor/L3 plugins
  - Sample 'ACMECorp' plugin + README.plugins in documentation directory.
- Localization/Internationalization:
  - Changes to support non-ASCII character input from character sets used in
    Red Hat GSS supported languages.

* Wed May 1 2013 Nigel Jones <nigjones@redhat.com> - 0.9.3-1
- Pagination bug fix to fix an offsetting bug that could contribute
  to missing, or duplicate results.

* Fri Apr 26 2013 Nigel Jones <nigjones@redhat.com> - 0.9.2-1
- Various updates to source, including:
  - Pagination of 'listcases'
  - Better debugability
  - Splitfile abilities to 'addattachment'
  - Recommendations support
  - Changes to 'downloadall' attachment handling

* Wed Feb 20 2013 Nigel Jones <nigjones@redhat.com> - 0.9.0-2
- Import into Red Hat packaging system

* Fri Apr 13 2012 Keith Robertson <kroberts@redhat.com> - 0.9.0-1
- Initial build
