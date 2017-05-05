# OceanKTV Kodi Plugins
Plugins for Kodi Media Player


## OceanKTV youtube-dl plugin upgrade

**更新步驟：**
1. new a branch
2. 將更新後的 plugin 壓縮成 zip 檔，並放到 releases 路徑下，plugin 的更新請參考 [Ocean-kod](https://github.com/qeek-dev/Ocean-kod)
3. 更改 KodiPlugins addons.xml 裡描述的 plugin 版本號碼
```xml
   <addon id="script.oceanktv.youtube.dl" name="oceanktv youtube-dl" version="17.918.0" provider-name="qnap">
```
4. push branch
5. NAS 重新安裝 OceanKTV qpkg (先不啟動 KTV)
6. 手動修改 NAS 上 OceanKTV 的 TVplayer youtube plugin xml，將內容指到 new branch

   vi /share/CACHEDEV1_DATA/.qpkg/KTVStation/player/repository.merlink.kodi-addons/addon.xml
```xml
    <extension name="Merlinks Unofficial Add-on Repository" point="xbmc.addon.repository">
        <info compressed="false">https://github.com/qeek-dev/KodiPlugins/raw/feature/remove-plugins/addons.xml</info>
<!--
        <checksum>link</checksum>
-->
        <datadir zip="true">https://github.com/qeek-dev/KodiPlugins/raw/feature/remove-plugins/releases</datadir>
<!--
        <hashes>true</hashes>
-->
    </extension>

```

7. 開啟 OceanKTV 稍等片刻後查看是否更新成功，更新成功可在下列路徑確定安裝的套件版本
```
/share/CACHEDEV1_DATA/.qpkg/KTVStation/root/.kodi/addons/script.module.youtube.dl/addon.xml
```
8. 上述步驟完成沒問題後，即可 merge 回 master :+1:
