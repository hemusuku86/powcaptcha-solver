import ua_generator
import requests
import hashlib
import random
import base64
import gzip
import json
import time

def generateHash(components):
    return hashlib.sha256((json.dumps(components, separators=(',', ':'))+"{}").encode()).hexdigest()

def generateFingerprint(useragent):
    s = time.time()
    if "CriOS/" in useragent:
        crios = True
    else:
        crios = False
    # you should make more accurate fp emulator but im lazy
    components = {
   "applePay": 2 if crios else 0,
   "canvas":{
      "isPointInPath": True,
      "isPointNotInPath": False,
      "textMetricsWidth":199.3671875,
      "dataUrlHash":"c25526d5f52d6dd319b83b5f069de0f1b2a8fa6496e9a5aa44a178b4533e7a52"
   },
   "audio":{
      "fingerprint":3.861334452034953,
      "fudgeFactor":1
   },
   "browser":{
      "os": "macOS" if crios else "Windows 10",
      "mobile": True if crios else False,
      "tablet": False,
      "engine":"WebKit",
      "engineVersion":useragent.split("AppleWebKit/")[1].split(" "),
      "userAgent":useragent,
      "capabilities":{
         "serviceWorker": True,
         "webWorker": True,
         "webSocket": True,
         "webRTC": True,
         "webGL": True,
         "webP": True,
         "webAssembly": True,
         "webShare": True,
         "webNFC": False,
         "webUSB": False,
         "webBluetooth": True,
         "webMIDI": True,
         "webAuthentication": True,
         "webPayments": True,
         "webSpeech": True,
         "performance": True,
         "memoryInfo": True,
         "deviceMemory": True,
         "hardwareConcurrency":4,
         "localStorage": True,
         "sessionStorage": True,
         "indexedDB": True,
         "cacheAPI": True,
         "mediaDevices": True,
         "mediaSession": True,
         "mediaCapabilities": True,
         "secureContext": True,
         "crossOriginIsolated": False,
         "permissions": True
      },
      "kindDetectors":{
         "browserFeatureCount":{
            "1":6,
            "2":0,
            "3":0,
            "4":0,
            "5":0
         },
         "browsserKind":1
      },
      "platform": "Apple" if crios else "Win32",
      "vendor": "Apple Computer, Inc." if crios else "Google Inc.",
      "maxTouchPoints": 5 if crios else 0,
      "webdriver": False
   },
   "language":{
      "language":"ja"
   },
   "fonts":{
      "Arial":{
         "base":"2932x654",
         "emoji":"99x368"
      },
      "Calibri":{
         "base":"2580x704",
         "emoji":"99x379"
      },
      "Cambria":{
         "base":"2779x672",
         "emoji":"99x372"
      },
      "Comic Sans MS":{
         "base":"3086x800",
         "emoji":"99x400"
      },
      "Consolas":{
         "base":"2771x672",
         "emoji":"99x372"
      },
      "Courier New":{
         "base":"3025x656",
         "emoji":"99x382"
      },
      "Georgia":{
         "base":"2975x656",
         "emoji":"99x370"
      },
      "Helvetica":{
         "base":"2932x654",
         "emoji":"99x368"
      },
      "Segoe UI":{
         "base":"2825x768",
         "emoji":"99x384"
      },
      "Tahoma":{
         "base":"2837x696",
         "emoji":"99x375"
      },
      "Times New Roman":{
         "base":"2816x661",
         "emoji":"99x368"
      },
      "Verdana":{
         "base":"3234x696",
         "emoji":"99x375"
      }
   },
   "prefersReducedMotion": False,
   "plugins":{
      "items":{
         "0":{
            "0":{
               
            },
            "1":{
               
            }
         },
         "1":{
            "0":{
               
            },
            "1":{
               
            }
         },
         "2":{
            "0":{
               
            },
            "1":{
               
            }
         },
         "3":{
            "0":{
               
            },
            "1":{
               
            }
         },
         "4":{
            "0":{
               
            },
            "1":{
               
            }
         }
      },
      "length":5
   },
   "mathBehavior":{
      "mathPi":3.141592653589793,
      "mathE":2.718281828459045,
      "sinZero":0,
      "cosPI":-1,
      "tanPI":-1.2246467991473532e-16,
      "floatOperation":0.30000000000000004,
      "maxValue":0.30000000000000004,
      "infinity":None,
      "negativeInfinity":None,
      "nan":None,
      "roundPi":3,
      "floorPi":3,
      "ceilPi":4
   },
   "timezone":{
      "timezone":"Asia/Tokyo",
      "timezoneOffset":-540
   },
   "screen":{
      "availHeight":random.randint(800,899) if crios else random.randint(700,799),
      "availLeft":0,
      "availTop":0,
      "availWidth":random.randint(300,399) if crios else random.randint(1300,1399),
      "colorDepth":24,
      "isExtended": False,
      "orientation":{
         "angle":0,
         "type":"landscape-primary"
      },
      "pixelDepth":24,
      "width":1366
   },
   "webdriver": False,
   "webgl":{
      "vendor":"Apple Inc." if crios else "Google Inc. (Intel)",
      "renderer":"Apple GPU" if crios else "ANGLE (Intel, Intel(R) HD Graphics 620 (0x00005916) Direct3D11 vs_5_0 ps_5_0, D3D11)",
      "version":"WebGL 2.0" if crios else "WebGL 2.0 (OpenGL ES 3.0 Chromium)",
      "shadingLanguageVersion":"WebGL GLSL ES 3.00" if crios else "WebGL GLSL ES 3.00 (OpenGL ES GLSL ES 3.0 Chromium)",
      "supportedExtensions":[
         "EXT_clip_control",
         "EXT_color_buffer_float",
         "EXT_color_buffer_half_float",
         "EXT_conservative_depth",
         "EXT_depth_clamp",
         "EXT_disjoint_timer_query_webgl2",
         "EXT_float_blend",
         "EXT_polygon_offset_clamp",
         "EXT_render_snorm",
         "EXT_texture_compression_bptc",
         "EXT_texture_compression_rgtc",
         "EXT_texture_filter_anisotropic",
         "EXT_texture_mirror_clamp_to_edge",
         "EXT_texture_norm16",
         "KHR_parallel_shader_compile",
         "NV_shader_noperspective_interpolation",
         "OES_draw_buffers_indexed",
         "OES_sample_variables",
         "OES_shader_multisample_interpolation",
         "OES_texture_float_linear",
         "OVR_multiview2",
         "WEBGL_blend_func_extended",
         "WEBGL_clip_cull_distance",
         "WEBGL_compressed_texture_s3tc",
         "WEBGL_compressed_texture_s3tc_srgb",
         "WEBGL_debug_renderer_info",
         "WEBGL_debug_shaders",
         "WEBGL_lose_context",
         "WEBGL_multi_draw",
         "WEBGL_polygon_mode",
         "WEBGL_provoking_vertex",
         "WEBGL_stencil_texturing"
      ],
      "contextParameters":{
         "MAX_TEXTURE_SIZE":16384,
         "MAX_VIEWPORT_DIMS":[
            32767,
            32767
         ],
         "MAX_VERTEX_TEXTURE_IMAGE_UNITS":16,
         "MAX_TEXTURE_IMAGE_UNITS":16,
         "MAX_RENDERBUFFER_SIZE":16384,
         "MAX_CUBE_MAP_TEXTURE_SIZE":16384,
         "MAX_VERTEX_ATTRIBS":16,
         "MAX_VERTEX_UNIFORM_VECTORS":4096,
         "MAX_VARYING_VECTORS":30,
         "MAX_FRAGMENT_UNIFORM_VECTORS":1024,
         "ALIASED_LINE_WIDTH_RANGE":[
            1,
            1
         ],
         "ALIASED_POINT_SIZE_RANGE":[
            1,
            1024
         ]
      },
      "shaderPrecision":{
         
      }
   }
}
    if not crios:
        components["doNotTrack"] = None
        components["screen"]["height"] = components["screen"]["availHeight"] - 48
    else:
        components["language"]["languages"] = ["ja"]
        components["screen"]["height"] = components["screen"]["availHeight"]
    return json.dumps({
        "fingerprintId":generateHash(components),
        "components":components,
        "duration":int((time.time()-s)*1000)
    }, separators=(',', ':'))
    
def solveChallenge(challenge):
    started = time.time()
    signature = challenge["signature"]
    solutions = []
    for challengeItem in challenge["challenges"]:
        problem = challengeItem["problem"]
        difficulty = challengeItem["difficulty"]
        n = 0
        while True:
            if hashlib.sha256((signature + problem + str(n)).encode()).hexdigest().startswith("0"*difficulty):
                solutions.append(n)
                break
            n += 1
    return json.dumps({"challenge_id":challenge["id"],"solutions":solutions,"time":int((time.time() - started)*1000)}, separators=(',', ':'))

def solve(app_id, url):
    ua = ua_generator.generate(browser="chrome",platform=("windows","ios")).text
    data = {
        "app_id": app_id,
        "fingerprint": base64.b64encode(generateFingerprint(ua).encode()).decode(),
        "signals": {}
    }
    compressedData = gzip.compress(json.dumps(data, separators=(',', ':')).encode("ansi"))
    r=requests.post("https://api.powcaptcha.com/challenges/create",headers={
        "Content-Type": "application/json",
        "Content-Encoding": "gzip",
        "origin": f"{url.split('://')[0]}://{url.split('/')[2]}",
        "referer": url if url.endswith("/") else f"{url}/",
        "user-agent": ua
    }, data=compressedData)
    if r.json()["success"] != True:
        return r.json()
    return base64.b64encode(solveChallenge(r.json()["data"]).encode()).decode()
