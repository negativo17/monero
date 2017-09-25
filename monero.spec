# Running tests requires ~30 minutes and a fully synced blockchain
%global with_tests 0

Name:           monero
Version:        0.11.0.0
Release:        1%{?dist}
Summary:        Monero: the secure, private, untraceable cryptocurrency

License:        BSD
URL:            https://getmonero.org
Source0:        https://github.com/monero-project/%{name}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires:  boost-devel
BuildRequires:  cmake
BuildRequires:  doxygen
BuildRequires:  expat-devel
BuildRequires:  gcc
BuildRequires:  graphviz
BuildRequires:  gtest-devel
BuildRequires:  ldns-devel
BuildRequires:  libunwind-devel
BuildRequires:  lzma-devel
BuildRequires:  miniupnpc-devel
BuildRequires:  openssl-devel
#BuildRequires:  rapidjson-devel
BuildRequires:  readline-devel
BuildRequires:  unbound-devel
#BuildRequires:  pkg-config
#Requires:       

%description
Monero is a private, secure, untraceable, decentralised digital currency. You
are your bank, you control your funds, and nobody can trace your transfers
unless you allow them to do so.

Privacy: Monero uses a cryptographically sound system to allow you to send and
receive funds without your transactions being easily revealed on the blockchain
(the ledger of transactions that everyone has). This ensures that your
purchases, receipts, and all transfers remain absolutely private by default.

Security: Using the power of a distributed peer-to-peer consensus network,
every transaction on the network is cryptographically secured. Individual
wallets have a 25 word mnemonic seed that is only displayed once, and can be
written down to backup the wallet. Wallet files are encrypted with a passphrase
to ensure they are useless if stolen.

Untraceability: By taking advantage of ring signatures, a special property of a
certain type of cryptography, Monero is able to ensure that transactions are not
only untraceable, but have an optional measure of ambiguity that ensures that
transactions cannot easily be tied back to an individual user or computer.

%prep
%autosetup

%build
%cmake \
  -DBOOST_IGNORE_SYSTEM_PATHS=OFF \
  -DBUILD_DOCUMENTATION=ON \
  -DBUILD_GUI_DEPS=OFF \
  -DBUILD_TESTS=ON \
  -DSTATIC=OFF \
  -DUSE_READLINE=ON \
  .

%make_build

%if %with_tests
%check
make test
%endif

%install
%make_install

%files
%license LICENSE
%doc CONTRIBUTING.md README.i18n.md README.md VULNERABILITY_RESPONSE_PROCESS.md
%{_bindir}/monero-wallet-cli
%{_bindir}/monero-wallet-rpc
%{_bindir}/monerod

%changelog
* Fri Sep 22 2017 Simone Caronni <negativo17@gmail.com> - 0.11.0.0-1
- First build.
