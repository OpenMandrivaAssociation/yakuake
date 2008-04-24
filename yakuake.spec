Summary:	Very powerful Quake style Konsole
Name:		yakuake
Version:	2.9.2
Release:	%mkrel 1
License:	GPLv2+
Group:		Graphical desktop/KDE
Source:		http://download.berlios.de/%{name}/%{name}-%{version}.tar.bz2
Url:		http://www.kde-apps.org/content/show.php?content=29153
BuildRequires:	kdelibs4-devel
Requires:       konsole
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
Obsoletes:      kde4-%name <= 2.9.2
Provides:       kde4-%name = %version

%description
Yakuake is a Quake-style terminal emulator based on KDE Konsole technology.

%post
%{update_menus}
%update_icon_cache hicolor

%postun
%{clean_menus}
%clean_icon_cache hicolor

%files -f %{name}.lang
%defattr(-,root,root,-)
%doc AUTHORS ChangeLog README TODO NEWS KDE4FAQ
%{_kde_bindir}/*
%{_kde_datadir}/applications/kde4/*.desktop
%{_kde_appsdir}/%{name}
%{_kde_iconsdir}/hicolor/*/apps/*


#--------------------------------------------------------------------

%prep 
%setup -qn %{name}-%{version}

%build
%cmake_kde4
%make

%install
rm -rf %{buildroot}
cd build
%makeinstall_std
cd -

%find_lang %name

%clean 
rm -rf %{buildroot} 
