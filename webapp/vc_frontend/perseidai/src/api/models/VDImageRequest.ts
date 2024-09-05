/* generated using openapi-typescript-codegen -- do not edit */
/* istanbul ignore file */
/* tslint:disable */
/* eslint-disable */
import type { VDImageModelEnum } from './VDImageModelEnum';
export type VDImageRequest = {
    /**
     * The ML model for detecting vehicles
     *
     * * `YOLOv5s` - YOLOV5S
     * * `YOLOv8s` - YOLOV8S
     */
    model?: VDImageModelEnum;
    /**
     * The image file to be uploaded
     */
    image: Blob;
};

