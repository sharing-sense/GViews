# Copyright (c) 2012 The Chromium Authors. All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.

{
  'targets': [
    {
      'target_name': 'libpng',
      'dependencies': [
        '../zlib/zlib.gyp:zlib',
      ],
      'defines': [
        'CHROME_PNG_WRITE_SUPPORT',
        'PNG_USER_CONFIG',
      ],
      'sources': [
        'png.c',
        'png.h',
        'pngconf.h',
        'pngerror.c',
        'pnggccrd.c',
        'pngget.c',
        'pngmem.c',
        'pngpread.c',
        'pngread.c',
        'pngrio.c',
        'pngrtran.c',
        'pngrutil.c',
        'pngset.c',
        'pngtrans.c',
        'pngusr.h',
        'pngvcrd.c',
        'pngwio.c',
        'pngwrite.c',
        'pngwtran.c',
        'pngwutil.c',
      ],
      'direct_dependent_settings': {
        'include_dirs': [
          '.',
        ],
        'defines': [
          'CHROME_PNG_WRITE_SUPPORT',
          'PNG_USER_CONFIG',
        ],
      },
      'export_dependent_settings': [
        '../zlib/zlib.gyp:zlib',
      ],
      # TODO(jschuh): http://crbug.com/167187
      'msvs_disabled_warnings': [ 4267 ],
      'conditions': [
        ['OS!="win"', {'product_name': 'png'}],
        ['OS=="win"', {
          'type': 'static_library',
        }, {
          # Chromium libpng does not support building as a shared_library
          # on non-Windows platforms.
          'type': 'static_library',
        }],
        ['OS=="win" and component=="shared_library"', {
          'defines': [ 
            'PNG_NO_MODULEDEF',
          ],         
        }],
        ['OS=="android"', {
          'toolsets': ['target', 'host'],
        }],
      ],
    },
  ]
}
